from pydantic import Field, BaseModel
from typing import Annotated, List
from datetime import date


class BaseHistorySchema(BaseModel):
    name_operation: Annotated[str, Field(max_length=255)]
    date_operation: Annotated[date, Field()]


class AllHistoriesSchema(BaseModel):
    histories: Annotated[List[BaseHistorySchema], Field()]
