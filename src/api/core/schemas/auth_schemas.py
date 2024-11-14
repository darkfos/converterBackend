from pydantic import BaseModel, Field
from typing import Annotated


class TokensSchema(BaseModel):
    access_token: Annotated[str, Field()]
    refresh_token: Annotated[str, Field()]
