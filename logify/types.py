from datetime import datetime

from pydantic import BaseModel
from pydantic import Field


class RequestLog(BaseModel):
    date_time: datetime = Field(..., alias="dateTime")
    log: str
