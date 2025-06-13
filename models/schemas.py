import re

from pydantic import BaseModel, Field, HttpUrl, field_validator, model_validator
from typing import Optional
from datetime import datetime


class Flight(BaseModel):
    flight_uuid: str = Field(..., "md5 Checksum to quickly update status and actual flights time")
    flight_number: Optional[str] = Field(None, description= "Number of flight")
    airplane: Optional[str] = Field(None, description= "Airplane model number")
    origin: str = Field(..., description= "Departure Airport")
    destination: str = Field(..., description= "Arrival Airport")
    airline: Optional[str] = Field(None, description= "Airline that covers this flight")
    departure_time: datetime = Field(..., description= "Departure time in UTC")
    arrival_time: Optional[datetime] = Field(None, description= "Actual landing time in UTC")
    status: str = Field(..., description= "Status of the flight (On Time/Delayed/Cancelled)")
    scraped_at: HttpUrl = Field(..., description= "URL of data origin")
    
    
    @field_validator('status')
    def validate_status(cls, v: str) -> str:
        valid_statuses = ["On Time", "Delayed", "Cancelled"]
        
        if v not in valid_statuses:
            raise ValueError(f"Invalid status: { v }, must be one of { valid_statuses }")
        
        return v
    
    
    @field_validator('flight_number')
    def validate_flight_number(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        
        pattern = re.compile(r"^[A-Za-z].*\d$")
        if not pattern.match(v):
            raise ValueError("Flight number should begin with a letter and end with a number")
        
        return v
    
    
    @model_validator(mode= "after")
    def validate_times(self) -> "Flight":
         if self.arrival_time and self.arrival_time < self.departure_time:
             raise ValueError("Arrival time cannot be before departure time")
         
         return self