from typing import ClassVar

from pydantic import BaseModel, Field

from app.constant.ap_type import InterfaceSystemType


class CommonBody(BaseModel):
    siteId: str
    userId: str


class UiAgentBodyCommonVo(CommonBody):
    SRC: ClassVar[InterfaceSystemType] = InterfaceSystemType.UI
    TGT: ClassVar[InterfaceSystemType] = InterfaceSystemType.AGENT
    URI: ClassVar[str]


class AgentUiBodyCommonVo(CommonBody):
    SRC: ClassVar[InterfaceSystemType] = InterfaceSystemType.AGENT
    TGT: ClassVar[InterfaceSystemType] = InterfaceSystemType.UI
    retCode: str = Field(default="OK", description="Return Code")
    retComment: str = Field(None, description="Return Comment")
