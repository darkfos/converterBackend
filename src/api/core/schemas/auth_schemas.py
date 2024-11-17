from pydantic import BaseModel, Field, EmailStr
from typing import Annotated


class TokensSchema(BaseModel):
    access_token: Annotated[str, Field()]
    refresh_token: Annotated[str, Field()]


class RegistrationUser(BaseModel):
    email: Annotated[EmailStr, Field(min_length=6)]
    username: Annotated[str, Field(min_length=4, max_length=125)]
    password: Annotated[str, Field(min_length=8)]
