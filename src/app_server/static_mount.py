from pathlib import Path
from fastapi.staticfiles import StaticFiles
import logging
import os

logger = logging.getLogger(__name__)


def _relpath(path: Path, cwd: Path) -> str:
    try:
        return str(path.resolve().relative_to(cwd))
    except Exception:
        try:
            return os.path.relpath(str(path.resolve()), str(cwd))
        except Exception:
            return str(path)


def mount_static_and_assets(app, project_root: Path):
    """Mount local static directories used by the control panel and assets."""
    try:
        cwd = Path(os.getcwd()).resolve()
        logger.info(f"📂 CWD (server): {cwd}")
    except Exception as e:
        logger.warning(f"Could not resolve CWD: {e}")
        cwd = None

    static_dir = project_root / "src" / "static"
    assets_dir = project_root / "assets"
    docs_images_dir = project_root / "docs" / "images"

    if cwd:
        static_rel = _relpath(static_dir, cwd)
        assets_rel = _relpath(assets_dir, cwd)
        docs_images_rel = _relpath(docs_images_dir, cwd)
    else:
        static_rel = str(static_dir)
        assets_rel = str(assets_dir)
        docs_images_rel = str(docs_images_dir)

    if static_dir.exists():
        app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")
        logger.info("📎 Mounted /static → %s (relative: %s)", static_dir.resolve(), static_rel)
    else:
        logger.warning("⚠️ Static directory not found: %s", static_rel)

    if assets_dir.exists():
        app.mount("/assets", StaticFiles(directory=str(assets_dir)), name="assets")
        logger.info("📎 Mounted /assets → %s (relative: %s)", assets_dir.resolve(), assets_rel)
    else:
        logger.warning("⚠️ Assets directory not found: %s (relative: %s)", assets_dir, assets_rel)

    if docs_images_dir.exists():
        app.mount("/docs/images", StaticFiles(directory=str(docs_images_dir)), name="docs_images")
        logger.info("📎 Mounted /docs/images → %s (relative: %s)", docs_images_dir.resolve(), docs_images_rel)
    else:
        logger.info("ℹ️ docs/images directory not found: %s", docs_images_rel)
