from pydantic import BaseModel, EmailStr, validator


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: int = None
    is_subscribed: bool = False

    @validator("age")
    def check_age(cls, v):
        if v is not None and v < 0:
            raise ValueError("Age must be a positive integer")
        return v
