from typing import Optional

from pydantic import BaseModel, Field


class CommonQueryModel(BaseModel):
    enm: Optional[str] = Field(None, description="Event Name")
