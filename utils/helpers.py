import hashlib
import datetime


def generate_flight_uuid (flight_number: str, airplane: str, origin: str, destination: str, planned_departure_time: datetime, planned_arrival_time: datetime) -> str:
    raw = f"{ flight_number }|{ airplane }|{ origin }|{ destination }|{ planned_departure_time.isoformat() }|{ planned_arrival_time.isoformat() }"
    return hashlib.md5(raw.encode()).hexdigest()