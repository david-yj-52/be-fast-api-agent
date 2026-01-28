from typing import List, ClassVar

from pydantic import Field, BaseModel

from app.constant.ap_type import InterfaceSystemType
from app.model.interface.ap_body_common_vo import UiAgentBodyCommonVo, AgentUiBodyCommonVo


class UI_FETCH_PLTF_DEF(UiAgentBodyCommonVo):
    URI: ClassVar[str] = "/fetchPlatform"
    pass


class UI_NEW_PLTF_DEF_REQ(UiAgentBodyCommonVo):
    pltfNm: str = Field(None, description="Platform Name")
    pltfAlias: str = Field(None, description="Platform Alias")
    pltfBaseUrl: str = Field(..., description="Platform Base URL")

    SRC: ClassVar[InterfaceSystemType] = InterfaceSystemType.UI
    URI: ClassVar[str] = "/newPlatform"


class UI_NEW_PLTF_DEF_REP(AgentUiBodyCommonVo):
    pltfId: str = Field(..., description="Platform ID")
    pltfNm: str = Field(..., description="Platform Name")
    pltfAlias: str = Field(..., description="Platform Alias")
    pltfBaseUrl: str = Field(..., description="Platform Base URL")


class UI_NEW_PROD_INF_REQ_ELE_INF(BaseModel):
    eleNm: str = Field(..., description="Platform Name")
    eleTyp: str = Field(..., description="Platform Name")
    eleVal: str = Field(..., description="Platform Name")


class UI_NEW_PROD_INF_REQ(UiAgentBodyCommonVo):
    pltfId: str = Field(..., description="Platform ID")
    prodNm: str = Field(None, description="Platform Name")
    prodBaseUrl: str = Field(..., description="Platform Name")
    eleInfList: List[UI_NEW_PROD_INF_REQ_ELE_INF] = Field(..., description="추출 대상 Element 정보")

    URI: ClassVar[str] = "/newProduct"


class UI_NEW_PROD_INF_REP(AgentUiBodyCommonVo):
    pltfId: str = Field(..., description="Platform Id")
    prodId: str = Field(..., description="Product Name")
    prodNm: str = Field(..., description="Platform Name")
    prodBaseUrl: str = Field(..., description="Platform Name")
    eleInfList: List[UI_NEW_PROD_INF_REQ_ELE_INF] = Field(..., description="추출 대상 Element 정보")
