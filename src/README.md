# MCP Local Server — Source Layout

This directory contains the Python application code for the local MCP server.

## Main entry points

- `server.py` — Uvicorn entry point
- `app_factory.py` — FastAPI app creation
- `config.py` — environment loading and configuration helpers
- `ui_html.py` — control panel HTML integration

## Main subdirectories

- `app_core/` — shared runtime helpers (safe JSON, tool discovery)
- `app_server/` — FastAPI routes, static mounts, server assembly
- `tool_specs/` — canonical JSON specs for tools
- `tools/` — tool wrappers and internal implementations
- `static/` — static assets for the control panel
- `templates/control/` — control panel template components

## Tool model

Each tool is defined by:

1. a wrapper in `src/tools/`
2. a canonical JSON spec in `src/tool_specs/`
3. optionally, an internal implementation package under `src/tools/_<tool_name>/`

## Auto-generated catalog

The file:

```text
src/tools/README.md
```

is auto-generated from the JSON specs using:

```text
scripts/generate_tools_catalog.py
```

Do not edit `src/tools/README.md` manually.

## Notes

- This public repository intentionally excludes legacy internal runtime layers.
- The server is designed for local execution on `127.0.0.1:8000` by default.
- Tool discovery is driven by the Python wrappers and the canonical JSON specs.
