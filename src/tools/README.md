# 🧰 MCP Local Server Tools Catalog (auto‑généré)

Ce fichier est généré automatiquement par `scripts/generate_tools_catalog.py`. Ne pas éditer à la main.

Total tools: 20

## 🔧 Development (4)

- Dev Navigator — Couteau suisse LLM pour explorer un dépôt: overview, tree, search, outline, open (plan fs_requests uniquement — pas de contenu), endpoint… · Tags: knowledge
  - Opérations: compose, overview, tree, search, outline, open …
  - Tokens: aucun

- Playwright (Record & Play) — Enregistre une navigation via Playwright codegen (process.json live) et rejoue par ID (tout, jusqu’à une étape, ou une étape). Tous les f… · Tags: browser, record, replay
  - Opérations: record_start, record_list, record_delete, play
  - Tokens: aucun

- Python Sandbox — Exécute du code Python dans un sandbox sécurisé avec accès à des tools MCP. Pas d'imports, API limitée, timeout configurable.
  - Opérations: N/A
  - Tokens: aucun

- Shell Command — Execute shell commands (bash/sh). Useful for running scripts, tests, git commands, file operations. Supports piping, redirections, and wo… · Tags: shell, bash, command, exec, system
  - Opérations: N/A
  - Tokens: aucun

## 🗄️ Data & Storage (2)

- Excel to SQLite — Import Excel (.xlsx) data into SQLite database with automatic schema detection, type mapping, and batch processing
  - Opérations: import_excel, preview, get_sheets, validate_mapping, get_info
  - Tokens: aucun

- SQLite Database — Gestion d'une base SQLite locale dans <projet>/sqlite3. Créer, lister, supprimer des DB et exécuter des requêtes SQL. · Tags: sqlite, database, sql, local_storage
  - Opérations: ensure_dir, list_dbs, create_db, delete_db, get_tables, describe …
  - Tokens: aucun

## 📄 Documents (5)

- Doc Scraper — Universal documentation scraper supporting GitBook, Notion, Confluence, ReadTheDocs, Docusaurus, and other doc platforms. Discover, extra…
  - Opérations: discover_docs, extract_page, search_across_sites, detect_platform
  - Tokens: aucun

- Office to PDF Converter — Convert Microsoft Office documents (Word, PowerPoint) to PDF using either the Office suite installed on the laptop (via docx2pdf) or a he…
  - Opérations: convert, get_info
  - Tokens: aucun

- PDF Download — Télécharge un fichier PDF depuis une URL et le sauvegarde dans docs/pdfs. Gère automatiquement les conflits de noms avec suffixes numériq…
  - Opérations: download
  - Tokens: aucun

- PDF Search — Recherche texte dans un ou plusieurs PDFs. Hard cap à 50 résultats détaillés, affiche le total trouvé. Supporte regex, pages, récursif. · Tags: search, pdf, text
  - Opérations: search
  - Tokens: aucun

- PDF to Text — Extraction de texte depuis un PDF pour des pages données. Entrée: path (string), pages (string optionnelle) — Sortie: texte concaténé et…
  - Opérations: N/A
  - Tokens: aucun

## ✈️ Transportation (4)

- Aviation Weather — Get upper air weather data (winds, temperature) at specific altitude and coordinates using Open-Meteo API. Useful for flight planning and… · Tags: weather, aviation, flight
  - Opérations: get_winds_aloft, calculate_tas
  - Tokens: aucun

- Flight Tracker — Track aircraft in real-time using OpenSky Network API. Filter by position, radius, altitude, speed, country. Get live position, speed, he…
  - Opérations: track_flights
  - Tokens: aucun

- Ship Tracker — Suivi navires temps réel via AIS. Position, vitesse, cap, destination, type navire. Recherche par zone, MMSI ou port.
  - Opérations: track_ships, get_ship_details, get_port_traffic
  - Tokens: aucun

- Vélib' Métropole — Gestionnaire de cache Vélib' Métropole (Paris). Rafraîchit les données statiques des stations (stockées en SQLite), récupère la disponibi… · Tags: paris, bike_sharing, transport, realtime
  - Opérations: refresh_stations, get_availability, check_cache
  - Tokens: aucun

## 🌐 Networking (1)

- HTTP Client — Client HTTP/REST générique pour interagir avec n'importe quelle API. Supporte GET, POST, PUT, DELETE, PATCH, HEAD, OPTIONS avec authentif…
  - Opérations: N/A
  - Tokens: aucun

## 🔢 Utilities (3)

- Date/Time — Common date/time operations: weekday name, difference between dates, now/today, add duration, format, parse, week number. Supports timezo… · Tags: datetime, calendar, timezone
  - Opérations: now, today, day_of_week, diff, diff_days, add …
  - Tokens: aucun

- Math — Maths: arithmétique (précision arbitr.), expressions (SymPy), symbolique, complexes, probas (suppl.), algèbre linéaire (+ext), solveurs,…
  - Opérations: add, subtract, multiply, divide, power, modulo …
  - Tokens: aucun

- Open-Meteo — Complete weather data via Open-Meteo API (open source). Current weather, hourly/daily forecasts, air quality, geocoding. 100% free, no AP… · Tags: weather, forecast, air_quality, free
  - Opérations: current_weather, forecast_hourly, forecast_daily, air_quality, geocoding, reverse_geocoding
  - Tokens: aucun

## 🎮 Social & Entertainment (1)

- Lichess (Public API) — Accès en lecture seule aux endpoints publics de Lichess: profils, perfs, équipes, parties, tournois, leaderboards, puzzles. Sans authenti… · Tags: chess, lichess, public_api
  - Opérations: get_user_profile, get_user_perfs, get_user_teams, get_user_current_game, get_user_games, get_team_details …
  - Tokens: aucun
