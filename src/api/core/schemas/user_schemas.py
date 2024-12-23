from datetime import date
from pydantic import BaseModel, Field
from typing import Annotated, List


class UserBaseSchema(BaseModel):
    email: Annotated[str, Field(max_length=200)]
    username: Annotated[str, Field(max_length=125)]


class AllUsersSchema(BaseModel):
    users: Annotated[List[UserBaseSchema], Field()]


class NewUserSchema(UserBaseSchema):
    hashed_password: Annotated[str, Field(min_length=8)]


class AllInformationAboutUser(UserBaseSchema):
    user_type_name: Annotated[str, Field()]
    date_reg: Annotated[date, Field()]
