# Repository working rules

This repository contains canonical Biomedical RDM research content. Keep changes small, reviewable, and traceable to the approved task.

## Evidence and states

- Do not invent sources, DOI, identifiers, dates, legal claims, or research evidence.
- Closed bibliography is the target: every citation must resolve to a reviewed bibliography entry, and every entry must resolve to an authoritative source. Current state: 103 numbered entries exist, but the audit and legal QA are still in progress; some rows remain `BIB_PENDING` or `VERIFIED_UNAUDITED`.
- Use `VERIFIED`, `BIB_PENDING`, `CONTENT_PENDING`, and `BLOCKED_INPUT` accurately. Never delete `[CẦN KIỂM CHỨNG]` or equivalent verification flags without evidence.
- Record the source and lookup date for every verification result. Keep unresolved inputs explicit.

## Branches and review

- One task, one neutral branch, one worktree, one pull request. Use neutral prefixes such as `feat/`, `docs/`, `chore/`, or `fix/`.
- Do not push directly to `main` or merge before approval.
- Ask before a change could affect scope, scientific meaning, legal interpretation, data handling, architecture, or acceptance criteria. Document reversible low-impact assumptions.
- Do not include secrets, API keys, credentials, patient data, or other PII. Do not credit AI tools in commits, pull requests, README files, or the published site.

## Definition of done

- Documentation or content: review diff, preserve verification flags, check links and claims against authoritative sources, and run the relevant render.
- Course or quiz changes: render the affected pages and verify module and quiz counts.
- Bibliography changes: run `python scripts/audit_references.py`; inspect `references/AUDIT-REPORT.md`; run the applicable metadata verification separately.
- Literature review changes: run `quarto render` and record the result. Do not treat metadata lookup as claim verification.
- Legal changes: use primary government, parliamentary, official gazette, EUR-Lex, or eCFR sources; record the exact URL, date checked, and any limitation.

## Working principles

1. State assumptions and conflicts before editing.
2. Prefer the smallest implementation that satisfies the approved plan.
3. Make surgical changes; record unrelated findings instead of fixing them silently.
4. Define verification before implementation and use evidence appropriate to the change.
5. Ask rather than guess when uncertainty could change scope, science, law, data, architecture, or acceptance criteria.
6. Treat privacy, ethics, security, and legal compliance as controls across the full research-data lifecycle.
