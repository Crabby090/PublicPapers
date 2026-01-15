# AGENTS.md - PublicPapers

Mission
- Build and document autonomous academic papers as a public tech demonstrator.

Operating rules
- Create one paper per folder under `papers/<year>/<slug>/`.
- Use `scripts/new-paper.ps1` to scaffold new papers when possible.
- Keep work in Markdown (`paper.md`, `outline.md`, `notes.md`).
- Cite every non-trivial claim using numeric references like [1].
- Maintain `sources.md` with full citations and access dates.
- Maintain `claims.csv` so key claims map to sources and quotes.
- Do not fabricate citations, quotes, or data. If uncertain, mark as TODO.
- Keep `metadata.yml` current, including `status`.
- Export compiled artifacts to `exports/` only after checklist completion.

Workflow (default)
1. Scope the research question in `outline.md`.
2. Collect sources and populate `sources.md` and `claims.csv`.
3. Draft in `paper.md` with inline citations [n].
4. Self-review using `checklist.md` and update `metadata.yml` status.
5. Export to `exports/` if ready to share.

If blocked
- Leave a short note in `notes.md` with the blockage and next step.
