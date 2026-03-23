# LLM DEV GUIDE — MCP Local Server

Technical guide for LLM-assisted development on this repository.

---

## Purpose

This repository contains a public local MCP server with a selected packaged toolset.

Key constraints:
- keep the selected tools iso-functional
- keep the repository public-safe
- preserve the canonical specs workflow
- preserve auto-generated tools documentation
- do not reintroduce excluded legacy internal layers into this public repo

---

## Core architecture

Main files:
- `src/server.py` — server entry point
- `src/app_factory.py` — FastAPI app assembly
- `src/config.py` — environment helpers
- `src/tools/` — tool wrappers
- `src/tool_specs/` — canonical JSON specs
- `scripts/generate_tools_catalog.py` — generates `src/tools/README.md`

Main endpoints:
- `GET /tools`
- `POST /execute`
- `GET /control`
- `GET /config`
- `POST /config`

---

## Canonical rules

### Tool specs
- canonical source of truth = `src/tool_specs/*.json`
- `function.parameters` must be an object
- arrays must always define `items`
- prefer strict schemas where possible
- do not duplicate the canonical schema in Python when avoidable

### Tool wrappers
- expose `run(**params)` or equivalent explicit signature
- expose `spec() -> dict`
- avoid import-time side effects
- keep wrapper logic small when possible

### Auto-generated tools catalog

The file:

```text
src/tools/README.md
```

is auto-generated.

Rules:
- do not edit it manually
- edit the JSON specs instead
- regenerate via:

```bash
python3 scripts/generate_tools_catalog.py
```

The dev scripts may trigger this automatically.

---

## Public repository constraints

This repository is intended to be public.

Always avoid:
- secrets
- private infrastructure references
- internal-only URLs
- undocumented local hacks
- dead references to excluded legacy internal layers

---

## Documentation policy

Keep these documents aligned:
- `README.md`
- `src/README.md`
- `LLM_DEV_GUIDE.md`

If the tool list changes:
- update specs
- regenerate `src/tools/README.md`
- update public docs if needed

---

## Packaging policy

The project must remain easy to install locally:
- clean virtual environment
- clear `pyproject.toml`
- clear `.env.example`
- simple startup on localhost:8000

---

## Selected toolset

This repository currently targets the following tools:
- academic_research_super
- aviation_weather
- date
- dev_navigator
- excel_to_sqlite
- ffmpeg_frames
- flight_tracker
- http_client
- lichess
- math
- minecraft_control
- news_aggregator
- office_to_pdf
- open_meteo
- pdf2text
- pdf_download
- pdf_search
- playwright
- script_executor
- shell
- ship_tracker
- sqlite_db
- stockfish_auto
- tool_audit
- universal_doc_scraper
- velib
