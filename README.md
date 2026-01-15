# PublicPapers

A public repo for demonstrating autonomous academic research by LLMs.

## Goals
- Show an end-to-end, repeatable paper workflow that an agent can run autonomously.
- Keep evidence and citations transparent and auditable.
- Produce shareable artifacts (Markdown and exported documents).

## Structure
- `papers/` - one folder per paper under `papers/<year>/<slug>/`
- `templates/` - scaffolding files copied into new papers
- `scripts/` - helper scripts (e.g., scaffolding)
- `AGENTS.md` - operating instructions for agents in this repo

## Data and provenance (2025 tariffs and later)
This repo includes a 2025+ U.S. tariff communications snapshot under:
- `papers/2026/industry-responses-to-tariffs/data/sources/`

Provenance for that dataset:
- White House presidential actions, fact sheets, annex PDFs, and joint statements (official publications).
- GovInfo Federal Register and Daily Compilation of Presidential Documents (official publications).
- U.S. Customs and Border Protection Cargo Systems Messaging Service (CSMS) guidance (official publications).
- The American Presidency Project archive of Trump Truth Social posts.

Each item is listed with full citation and access date in:
- `papers/2026/industry-responses-to-tariffs/sources.md`

Key claims and supporting quotes are mapped in:
- `papers/2026/industry-responses-to-tariffs/claims.csv`

## Quickstart
Create a new paper scaffold:

```powershell
pwsh scripts/new-paper.ps1 -Title "Your Paper Title"
```

Optional parameters:
- `-Slug "custom-slug"`
- `-Year 2026`

Then fill in:
- `metadata.yml`
- `outline.md`
- `sources.md`
- `claims.csv`
- `paper.md`

## Workflow (high level)
1. Define the research question in `outline.md`.
2. Collect sources and log evidence in `sources.md` and `claims.csv`.
3. Draft the manuscript in `paper.md` with citations [n].
4. Run the checklist and update `metadata.yml` status.
5. Export to `exports/` if ready to share.

## License
This repository is MIT licensed. Individual papers may specify their own license in `metadata.yml`.
