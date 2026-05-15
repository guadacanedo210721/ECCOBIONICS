from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AttendanceCheckIn(BaseModel):
    employee_id: int
    method: str = "qr"

class AttendanceCheckOut(BaseModel):
    employee_id: int
    method: str = "qr"

class AttendanceResponse(BaseModel):
    id: int
    user_id: int
    check_in: Optional[datetime]
    check_out: Optional[datetime]
    check_in_method: str
    is_late: bool
    hours_worked: int
    date: datetime

    class Config:
        from_attributes = True
