"""GovESB transport settings, read by coremis_app_integration. Off unless ESB_ENABLED=true."""
import json
import os

MUSE_ENVIRONMENT = os.environ.get("MUSE_ENVIRONMENT", "").strip().upper()

if os.environ.get("ESB_ENABLED", "false").strip().lower() == "true":
    ESB = {
        "ENABLED": True,
        "AUTH_URL": os.environ.get("ESB_AUTH_URL", ""),
        "ENGINE_URL": os.environ.get("ESB_ENGINE_URL", ""),
        "GRANT_TYPE": os.environ.get("ESB_GRANT_TYPE", "client_credentials"),
        "CLIENT_ID": os.environ.get("ESB_CLIENT_ID", ""),
        "CLIENT_SECRET": os.environ.get("ESB_CLIENT_SECRET", ""),
        "CLIENT_PRIVATE_KEY": os.environ.get("ESB_CLIENT_PRIVATE_KEY", ""),
        "CLIENT_PUBLIC_KEY": os.environ.get("ESB_CLIENT_PUBLIC_KEY", ""),
        "GOV_ESB_PUBLIC_KEY_B64": os.environ.get("ESB_GOV_PUBLIC_KEY_B64", ""),
        "REQUEST_TIMEOUT": int(os.environ.get("ESB_REQUEST_TIMEOUT", "30")),
        "VERIFY_RESPONSE_SIGNATURE": os.environ.get("ESB_VERIFY_RESPONSE_SIGNATURE", "true").lower() == "true",
        "VERIFY_INBOUND_SIGNATURE": os.environ.get("ESB_VERIFY_INBOUND_SIGNATURE", "true").lower() == "true",
        "API_CODES": json.loads(os.environ.get("ESB_API_CODES", "{}") or "{}"),
    }
