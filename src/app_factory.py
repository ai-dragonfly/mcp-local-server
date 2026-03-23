from __future__ import annotations

from fastapi import FastAPI

from app_server.app_factory_compact import create_app as create_app_compact


# Public local-server entrypoint.
# Excluded legacy internal runtime layers are intentionally not part of this repository.

def create_app() -> FastAPI:
    return create_app_compact()
