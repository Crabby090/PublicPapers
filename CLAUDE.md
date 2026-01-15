# CLAUDE.md - PublicPapers

This repository demonstrates autonomous academic research by LLMs. Claude should follow these instructions when working here.

## Project Purpose

Build and document autonomous academic papers as a public tech demonstrator, with transparent evidence trails and auditable citations.

## Directory Structure

```
papers/<year>/<slug>/    # Individual paper folders
  ├── metadata.yml       # Title, status, authors, license
  ├── outline.md         # Research question and structure
  ├── paper.md           # Main manuscript with [n] citations
  ├── sources.md         # Full citations with access dates
  ├── claims.csv         # Claim → source → quote mapping
  ├── notes.md           # Working notes and blockers
  ├── checklist.md       # Pre-publish quality checklist
  ├── data/              # Raw data files
  ├── figures/           # Images and charts
  └── exports/           # Final artifacts (PDF, DOCX)
templates/               # Scaffold templates for new papers
scripts/                 # Helper scripts
```

## Quick Commands

Create a new paper scaffold:
```powershell
pwsh scripts/new-paper.ps1 -Title "Your Paper Title"
```

Optional parameters: `-Slug "custom-slug"`, `-Year 2026`

## Workflow

1. **Scope**: Define research question in `outline.md`
2. **Gather**: Collect sources in `sources.md`, log evidence in `claims.csv`
3. **Draft**: Write manuscript in `paper.md` with inline citations [n]
4. **Review**: Complete `checklist.md`, update `metadata.yml` status
5. **Export**: Generate final artifacts to `exports/` when ready

## Critical Rules

- **Never fabricate citations, quotes, or data** - mark uncertain items as TODO
- **Cite every non-trivial claim** using numeric references like [1]
- **Maintain `claims.csv`** so key claims map directly to sources and quotes
- **Keep `metadata.yml` current**, especially the `status` field
- **Use Markdown** for all primary content (paper.md, outline.md, notes.md)
- **If blocked**, leave a note in `notes.md` with the issue and proposed next step

## Citation Format

In `paper.md`:
```markdown
This claim is supported by evidence [1].
```

In `sources.md`:
```markdown
[1] Author. "Title." Publication, Date. URL (accessed YYYY-MM-DD).
```

In `claims.csv`:
```csv
claim,source_id,quote,page
"Key claim text",1,"Direct quote from source","p. 42"
```

## Status Values

Use these in `metadata.yml`:
- `draft` - Work in progress
- `review` - Ready for quality check
- `complete` - Checklist passed, ready to export
- `published` - Final artifact generated

## Working With Existing Documents

The repo may contain source documents (e.g., `.docx` files) for analysis. When processing these:
1. Read and summarize key points
2. Extract relevant quotes with page/section references
3. Log findings in `sources.md` and `claims.csv`
4. Reference in `paper.md` with proper citations
