<p align="center">
  <img src="assets/logo.svg" alt="MCP Local Server" width="160" />
</p>

# MCP Local Server

Public local MCP server with a packaged toolset and a web control panel.

This repository provides a clean, local-first server designed to run on your machine with:

- a dedicated Python virtual environment
- a local `.env` configuration file
- a web control panel
- a packaged set of validated local tools

By default, the recommended local endpoint is:

- `http://127.0.0.1:8000`

---

## What this project is

This project is a public-ready local MCP server extracted and cleaned from a larger internal codebase.

The repository now focuses on a stable public toolset and a simple local execution model.

It is intended to help users:

- install a local MCP server cleanly
- start it
- restart it after configuration changes
- browse and test tools through a local control panel

---

## Included tools

The current public toolset contains **20 tools**:

- aviation_weather
- date
- dev_navigator
- excel_to_sqlite
- flight_tracker
- http_client
- lichess
- math
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
- universal_doc_scraper
- velib

For the generated tools catalog, see:

- `src/tools/README.md`

> `src/tools/README.md` is auto-generated from the tool specs. Do not edit it manually.

---

## Requirements

- Python **3.10+** required
- Python **3.11 recommended**
- macOS, Linux, or Windows

Some tools require additional local software or external credentials.

Examples:

- `playwright` may require browser installation
- `office_to_pdf` may depend on local Office or LibreOffice availability
- `ship_tracker` requires an AISStream API key
- tools using external services may require credentials in `.env`

---

## Quickstart

### 1. Clone the repository

```bash
git clone https://github.com/ai-dragonfly/mcp-local-server.git
cd mcp-local-server
```

### 2. Create a virtual environment

#### macOS / Linux
```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

#### Windows PowerShell
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

> If `python3.11` is not available on your machine, use any Python 3.10+ interpreter.

### 3. Install dependencies

```bash
pip install --upgrade pip
pip install -e .
```

### 4. Create your local environment file

```bash
cp .env.example .env
```

Then edit `.env` only if needed.

### 5. Start the server

#### macOS / Linux
```bash
./scripts/dev.sh
```

#### Windows PowerShell
```powershell
./scripts/dev.ps1
```

Or run directly:

```bash
python src/server.py
```

---

## First-run validation

After startup, validate that the server responds correctly:

```bash
curl http://127.0.0.1:8000/tools
```

You can also open:

- Control panel: `http://127.0.0.1:8000/control`
- Tools registry: `http://127.0.0.1:8000/tools`

---

## Local URLs

Once started, the server is available at:

- Control panel: `http://127.0.0.1:8000/control`
- Tools registry: `http://127.0.0.1:8000/tools`
- Tool execution endpoint: `http://127.0.0.1:8000/execute`

---

## Restarting the server

If you change code, specs, or environment settings, stop the process and start it again.

### Important
If you modify `.env`, you must restart the server before testing again.

Standard restart flow:

```bash
# stop current server
# reactivate venv if needed
source .venv/bin/activate
python src/server.py
```

If you use the provided dev scripts, re-run them the same way as the first start.

---

## Calling a tool

Tools are executed through the `/execute` endpoint with a JSON payload.

Example:

```json
{
  "tool": "date",
  "params": {
    "operation": "now",
    "tz": "UTC"
  }
}
```

Example with `http_client`:

```json
{
  "tool": "http_client",
  "params": {
    "method": "GET",
    "url": "https://api.github.com"
  }
}
```

Example with `sqlite_db`:

```json
{
  "tool": "sqlite_db",
  "params": {
    "operation": "list_dbs"
  }
}
```

---

## Tool discovery

You can discover tools in two ways:

- through the web control panel at `/control`
- through the registry endpoint at `/tools`

Canonical tool specs are stored in:

```text
src/tool_specs/*.json
```

---

## Auto-generated tools catalog

The file:

```text
src/tools/README.md
```

is auto-generated from the tool specs using:

```text
scripts/generate_tools_catalog.py
```

Do not edit `src/tools/README.md` manually.

To regenerate it:

```bash
python3 scripts/generate_tools_catalog.py
```

---

## Tool-specific notes

### `ship_tracker`
This tool requires an AISStream API key.

To use it, define in `.env`:

```dotenv
AISSTREAM_API_KEY=...
```

### `office_to_pdf`
This tool expects files under:

```text
docs/office/
```

### `pdf_download`
Downloaded PDFs are stored under:

```text
docs/pdfs/
```

---

## Project structure

```text
src/
  server.py
  app_factory.py
  config.py
  app_core/
  app_server/
  tool_specs/
  tools/
  static/
  templates/control/
```

See also:

- `src/README.md`
- `LLM_DEV_GUIDE.md`

---

## Environment configuration

The repository includes a public-safe example configuration file:

```text
.env.example
```

Create your own local config with:

```bash
cp .env.example .env
```

Do not commit your `.env` file.

---

## Notes

- This project is designed for local use.
- Tool availability may depend on your machine configuration.
- Some tools require optional local software or external credentials.
- Review `.env.example` before using tools that depend on external services.

---

## Development

Useful commands:

```bash
python3 scripts/generate_tools_catalog.py
python src/server.py
```

If you use the provided dev scripts, the tools catalog generation is handled automatically.

---

## License

MIT
