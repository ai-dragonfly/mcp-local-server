#!/usr/bin/env python3
import os
import sys
import logging
import uvicorn
from fastapi import FastAPI


def load_local_env() -> None:
    """Load .env as early as possible so runtime config (host/port/log level)
    is honored when launching the server directly.
    """
    try:
        from dotenv import load_dotenv, find_dotenv  # type: ignore
        dotenv_path = find_dotenv(usecwd=True)
        if dotenv_path:
            load_dotenv(dotenv_path, override=True)
            return
    except Exception:
        pass

    env_path = os.path.join(os.getcwd(), '.env')
    if os.path.isfile(env_path):
        try:
            with open(env_path, 'r', encoding='utf-8') as f:
                for line in f:
                    s = line.strip()
                    if not s or s.startswith('#') or '=' not in s:
                        continue
                    k, v = s.split('=', 1)
                    k = k.strip()
                    v = v.strip().strip('"').strip("'")
                    os.environ[k] = v
        except Exception:
            pass


def get_server_host() -> str:
    return os.getenv('MCP_HOST', '127.0.0.1').strip() or '127.0.0.1'


def get_server_port() -> int:
    raw = (os.getenv('MCP_PORT', '8000') or '8000').strip()
    try:
        port = int(raw)
    except Exception:
        port = 8000
    if port < 1 or port > 65535:
        port = 8000
    return port


load_local_env()

if os.path.isdir('src') and 'src' not in sys.path:
    sys.path.insert(0, 'src')

logging.basicConfig(
    level=os.getenv('LOG_LEVEL', 'INFO').upper(),
    format='%(levelname)s:     %(message)s',
    handlers=[logging.StreamHandler()]
)

from app_factory import create_app

app: FastAPI = create_app()

if __name__ == "__main__":
    uvicorn.run(
        app,
        host=get_server_host(),
        port=get_server_port(),
        reload=False,
        log_level=os.getenv('LOG_LEVEL', 'info').lower(),
        access_log=False
    )
