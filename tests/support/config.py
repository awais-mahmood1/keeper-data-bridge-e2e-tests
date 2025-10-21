import os
from dataclasses import dataclass

@dataclass(frozen=True)
class ApiSettings:
    base_url: str = os.getenv("API_BASE_URL", "https://ls-keeper-data-bridge-backend.dev.cdp-int.defra.cloud")
    health_path: str = os.getenv("HEALTH_PATH", "/health")
    upload_path: str = os.getenv("UPLOAD_PATH", "/api/sourcedata/upload")
    auth_type: str = os.getenv("AUTH_TYPE", "None")
    bearer_token: str = os.getenv("BEARER_TOKEN", "")
    field_name: str = os.getenv("ENCRYPTED_FILE_FIELD_NAME", "file")
    upload_filename: str = os.getenv("ENCRYPTED_FILE_UPLOAD_FILENAME", "sample.csv.enc")
    content_type: str = os.getenv("ENCRYPTED_FILE_CONTENT_TYPE", "application/octet-stream")
    checksum_header_name: str = os.getenv("CHECKSUM_HEADER_NAME", "X-Checksum-MD5")
    verify_via: str = os.getenv("VERIFY_VIA", "none")

@dataclass(frozen=True)
class DataSettings:
    abs_path: str = os.getenv("ENCRYPTED_FILE_PATH", "")
    rel_path: str = os.getenv("ENCRYPTED_FILE_REL", "sample.csv")

@dataclass(frozen=True)
class S3Settings:
    region: str = os.getenv("AWS_REGION", "eu-west-2")
    bucket: str = os.getenv("S3_BUCKET", "")
    key_prefix: str = os.getenv("S3_KEY_PREFIX", "processed/")
    poll_seconds_total: int = int(os.getenv("POLL_SECONDS_TOTAL", "180"))
    poll_interval_seconds: int = int(os.getenv("POLL_INTERVAL_SECONDS", "5"))