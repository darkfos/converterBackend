from pydantic import BaseModel, Field
from typing import Annotated, List


class UserTypeBaseSchema(BaseModel):
    id_user_type: Annotated[int, Field(gt=0)]
    user_type_name: Annotated[str, Field(max_length=120)]


class AllUserTypes(BaseModel):
    user_types: Annotated[List[UserTypeBaseSchema], Field()]
