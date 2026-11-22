#!/usr/bin/env python3
"""Validate chapter and capstone quizzes using only the Python standard library."""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

ABSOLUTE = re.compile(
    r"\b(luôn|chỉ|mọi|không bao giờ|hoàn toàn|tuyệt đối|bắt buộc|tất cả|duy nhất|không thể)\b",
    re.IGNORECASE,
)


ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = [ROOT / "docs" / "chapters" / f"ch0{i}_" for i in range(1, 7)]
EXPECTED = {1: 5, 2: 4, 3: 5, 4: 5, 5: 4, 6: 6}
LETTERS = "ABCD"


def chapter_path(number: int) -> Path:
    matches = sorted((ROOT / "docs" / "chapters").glob(f"ch0{number}_*.md"))
    if len(matches) != 1:
        raise ValueError(f"expected one chapter file for ch{number:02d}, found {len(matches)}")
    return matches[0]


def question_records(text: str, chapter: int) -> list[dict[str, object]]:
    if chapter == 7:
        start = text.find("## PHẦN 1.")
        end = text.find("## PHẦN 2.")
        if start < 0 or end < 0:
            raise ValueError("ch07 is missing the aggregate quiz section")
        text = text[start:end]
        pattern = re.compile(r"^\*\*Q(\d+)\.\*\*\s*(.*?)\s*$", re.M)
    else:
        header = re.search(
            r"^## Quiz tự kiểm tra — Bài " + str(chapter) + r" \((\d+) câu hỏi\)\s*$",
            text,
            re.M,
        )
        if not header:
            raise ValueError(f"ch{chapter:02d} is missing its quiz heading")
        declared = int(header.group(1))
        next_section = re.search(r"^## ", text[header.end() :], re.M)
        body_end = header.end() + next_section.start() if next_section else len(text)
        text = text[header.end() : body_end]
        pattern = re.compile(r"^### \*\*Câu (\d+\.\d+)\.\s*(.*?)\*\*\s*$", re.M)
        text = f"DECLARED:{declared}\n" + text

    matches = list(pattern.finditer(text))
    records = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        block = text[match.end() : end]
        options = {letter: option for letter, option in re.findall(r"^- ([A-D])\.\s*(.+?)\s*$", block, re.M)}
        answer_match = re.search(r"Đáp án(?: đúng)?:\s*([A-D])\.", block)
        explanation = re.search(r"Giải thích:\*?\s*(.+?)(?=\n\s*---|\Z)", block, re.S)
        if not explanation and answer_match:
            trailing = block[answer_match.end() :].strip()
            if trailing:
                explanation = True
        records.append(
            {
                "id": match.group(1),
                "options": options,
                "answer": answer_match.group(1) if answer_match else None,
                "explanation": (explanation.group(1).strip() if hasattr(explanation, "group") else "present") if explanation else "",
            }
        )
    return records


def validate(records: list[dict[str, object]], label: str, expected: int | None, errors: list[str]) -> Counter[str]:
    if expected is not None and len(records) != expected:
        errors.append(f"{label}: declared/expected {expected} questions but found {len(records)}")
    answers: Counter[str] = Counter()
    longest = 0
    correct_abs = 0
    wrong_abs = 0
    ratios: list[float] = []
    for record in records:
        question = f"{label} {record['id']}"
        options = record["options"]
        if set(options) != set(LETTERS):
            errors.append(f"{question}: requires exactly four A-D options")
            continue
        answer = record["answer"]
        if answer not in LETTERS:
            errors.append(f"{question}: missing or invalid correct answer")
            continue
        if not record["explanation"]:
            errors.append(f"{question}: missing explanation")
        answers[answer] += 1
        correct_length = len(str(options[answer]))
        wrong_lengths = [len(str(options[letter])) for letter in LETTERS if letter != answer]
        if correct_length > max(wrong_lengths):
            longest += 1
        ratios.append(correct_length / (sum(wrong_lengths) / len(wrong_lengths)))
        correct_abs += len(ABSOLUTE.findall(str(options[answer])))
        wrong_abs += sum(len(ABSOLUTE.findall(str(options[letter]))) for letter in LETTERS if letter != answer)
    # Absolute-wording giveaway: wrong options must not carry far more absolute
    # terms (luôn, chỉ, mọi, tuyệt đối...) than the correct one.
    if records and wrong_abs / (3 * len(records)) - correct_abs / len(records) > 0.25:
        errors.append(
            f"{label}: wrong options contain absolute wording much more often than the correct ones "
            f"({wrong_abs / (3 * len(records)):.2f} vs {correct_abs / len(records):.2f} per option; limit +0.25)"
        )
    # Length-based giveaway rules from the quiz brief (enforced, not advisory):
    # at most 40% of a chapter's correct answers may be the strictly longest
    # option, and the correct option must not be much longer than the wrong ones.
    if len(records) >= 4 and longest / len(records) > 0.40:
        errors.append(f"{label}: correct answer is the longest option in {longest}/{len(records)} questions (limit 40%)")
    if ratios and sum(ratios) / len(ratios) > 1.30:
        errors.append(f"{label}: mean correct/wrong option length ratio {sum(ratios) / len(ratios):.2f} exceeds 1.30")
    if len(records) >= 3 and sum(1 for letter in LETTERS if answers[letter]) < 3:
        errors.append(f"{label}: uses fewer than three answer letters")
    if records and any(count / len(records) > 0.50 for count in answers.values()):
        errors.append(f"{label}: one answer letter exceeds 50% ({dict(answers)})")
    return answers


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="return non-zero when a quiz rule fails")
    args = parser.parse_args()
    errors: list[str] = []
    all_answers: Counter[str] = Counter()
    rows: list[tuple[str, int, Counter[str]]] = []

    for number in range(1, 7):
        path = chapter_path(number)
        records = question_records(path.read_text(encoding="utf-8"), number)
        counts = validate(records, f"ch{number:02d}", EXPECTED[number], errors)
        all_answers.update(counts)
        rows.append((f"ch{number:02d}", len(records), counts))

    ch07 = ROOT / "docs" / "chapters" / "ch07_completion_and_capstone.md"
    records = question_records(ch07.read_text(encoding="utf-8"), 7)
    counts = validate(records, "ch07 aggregate", 10, errors)
    all_answers.update(counts)
    rows.append(("ch07", len(records), counts))

    total = sum(all_answers.values())
    if total and any(not 0.20 <= all_answers[letter] / total <= 0.30 for letter in LETTERS):
        errors.append(f"all quizzes: answer distribution outside 20-30% ({dict(all_answers)}, total={total})")

    print("Quiz counts and answer distribution")
    print("chapter  questions  A  B  C  D")
    for label, count, answers in rows:
        print(f"{label:7} {count:10}  " + "  ".join(str(answers[letter]) for letter in LETTERS))
    print(f"total   {total:10}  " + "  ".join(str(all_answers[letter]) for letter in LETTERS))
    if errors:
        print("\nVIOLATIONS")
        print("\n".join(f"- {error}" for error in errors))
        return 1 if args.check else 0
    print("\nPASS: quiz structure and distribution rules satisfied")
    return 0


if __name__ == "__main__":
    sys.exit(main())
