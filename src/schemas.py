from datetime import date, datetime
from typing import List, Optional
from pydantic import BaseModel, Field, EmailStr


class ContactBase(BaseModel):
    name: str = Field(max_length=30)
    fullname: str = Field(max_length=30)
    email: EmailStr
    phone_number: str
    birthday: date
    description: str = Field(max_length=150)


class ContactResponse(ContactBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
