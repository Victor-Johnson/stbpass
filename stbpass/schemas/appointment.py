from pydantic import BaseModel
from datetime import datetime

class AppointmentCreate(BaseModel):
    user_id: int
    house_id: int
    date_time: datetime

class AppointmentResponse(AppointmentCreate):
    id: int
    status: str

    class Config:
        from_attributes = True