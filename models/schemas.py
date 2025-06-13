from pydantic import BaseModel, Field, HttpUrl
from typing import Optional
from datetime import datetime

class Flight(BaseModel):
    flight_number: Optional[str] = Field(None, description= "Number of flight")
    airplane: Optional[str] = Field(None, description= "Airplane model number")
    origin: str = Field(..., description= "Departure Airport")
    destination: str = Field(..., description= "Arrival Airport")
    airline: Optional[str] = Field(None, description= "Airline that covers this flight")
    departure_time: datetime = Field(..., description= "Departure time in UTC")
    planned_arrival_time: datetime = Field(..., description= "Planned arrival time in UTC")
    landing_time: Optional[datetime] = Field(None, description= "Actual landing time in UTC")
    scraped_at: HttpUrl = Field(..., description= "URL of data origin")