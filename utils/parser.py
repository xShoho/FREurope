from datetime import datetime
from zoneinfo import ZoneInfo


def parse_utc(dt: datetime, from_tz: str = "Europe/Warsaw") -> datetime:
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo= ZoneInfo(from_tz))
    else:
        dt = dt.astimezone(ZoneInfo(from_tz))
        
    return dt.astimezone(ZoneInfo("UTC"))