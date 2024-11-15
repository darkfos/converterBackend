from pydantic import BaseModel, Field

from typing import Annotated, List


class UserBaseSchema(BaseModel):
    email: Annotated[str, Field(max_length=200)]
    avatar_url: Annotated[str, Field()]


class AllUsersSchema(BaseModel):
    users: Annotated[List[UserBaseSchema], Field()]


class NewUserSchema(UserBaseSchema):
    hashed_password: Annotated[str, Field(min_length=8)]