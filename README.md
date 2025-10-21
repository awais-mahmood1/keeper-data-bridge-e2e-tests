# Keeper Data Bridge – API Tests (Python)


## Requirements
- Python 3.11+
- Network access to the target environment (VPN or approved CI runner)

## Install
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Healthcheck
```bash
API_BASE_URL="https://ls-keeper-data-bridge-backend.dev.cdp-int.defra.cloud" \
HEALTH_PATH="/health" \AUTH_TYPE="None" \pytest -q -k test_health
```

### Configuration
**API**
- `API_BASE_URL` (default `https://ls-keeper-data-bridge-backend.dev.cdp-int.defra.cloud`)
- `HEALTH_PATH` (default `/health`)
- `UPLOAD_PATH` (default `/api/sourcedata/upload`)
- `AUTH_TYPE` (`None` or `Bearer`, default `None`)
- `BEARER_TOKEN` (set if `AUTH_TYPE=Bearer`)

**File**
- `ENCRYPTED_FILE_PATH` (absolute path) or
- `ENCRYPTED_FILE_REL` (relative to `tests/data/`, default `sample.csv`)
- `ENCRYPTED_FILE_FIELD_NAME` (default `file`)
- `ENCRYPTED_FILE_UPLOAD_FILENAME` (default `sample.csv.enc`)
- `ENCRYPTED_FILE_CONTENT_TYPE` (default `application/octet-stream`)

**Checksum**
- `CHECKSUM_HEADER_NAME` (default `X-Checksum-MD5`)
- `VERIFY_VIA` (`s3_metadata` | `etag` | `none`, default `none`)

**S3**
- `AWS_REGION` (default `eu-west-2`)
- `S3_BUCKET` (required when enabling S3 checks)
- `S3_KEY_PREFIX` (default `processed/`)
- `POLL_SECONDS_TOTAL` (default `180`)
- `POLL_INTERVAL_SECONDS` (default `5`)

## CI (GitHub Actions)
A workflow in `.github/workflows/tests.yml` runs the healthcheck on push/PR.