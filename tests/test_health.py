import httpx
from tests.support.config import ApiSettings

def test_health_returns_ok():
    cfg = ApiSettings()
    url = f"{cfg.base_url.rstrip('/')}{cfg.health_path}"
    headers = {}
    if cfg.auth_type.lower() == "bearer" and cfg.bearer_token:
        headers["Authorization"] = f"Bearer {cfg.bearer_token}"
    with httpx.Client(timeout=20) as c:
        r = c.get(url, headers=headers)
    assert r.status_code in (200, 204)