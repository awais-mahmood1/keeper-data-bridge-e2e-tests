import time
from typing import Optional
import boto3

def list_first_key_with_prefix(bucket: str, prefix: str, region: str) -> Optional[str]:
    s3 = boto3.client("s3", region_name=region)
    resp = s3.list_objects_v2(Bucket=bucket, Prefix=prefix, MaxKeys=1)
    contents = resp.get("Contents", [])
    return contents[0]["Key"] if contents else None

def poll_for_key(bucket: str, prefix: str, region: str, total_seconds: int, interval_seconds: int) -> Optional[str]:
    deadline = time.time() + total_seconds
    key = None
    while time.time() < deadline and not key:
        key = list_first_key_with_prefix(bucket, prefix, region)
        if key:
            return key
        time.sleep(interval_seconds)
    return None

def head_object_metadata(bucket: str, key: str, region: str):
    s3 = boto3.client("s3", region_name=region)
    resp = s3.head_object(Bucket=bucket, Key=key)
    return resp.get("Metadata", {}), resp.get("ETag", "").strip('"')