import logging
from pathlib import Path
from typing import Optional

from fastapi import APIRouter
from fastapi.params import Query

from app.config.config_manager import ConfigManager
from app.constant.ap_type import AgentStatus
from app.model.interface.ap_head_vo import HeadVo, generate_head_vo
from app.model.interface.ap_interface_vo import ApInterfaceVo
from app.model.interface.agent_loader_interface_model import AGENT_SYS_HEALTH_CHECK_REP

logger = logging.getLogger(__name__)
router = APIRouter(
    prefix="/sys_check",
    tags=["health"],
)

settings = ConfigManager()

@router.get("/health", response_model=ApInterfaceVo[AGENT_SYS_HEALTH_CHECK_REP])
async def get_agent_health_status(
        enm: Optional[str] = Query(None, description="Event name"),
):
    """
    ip:port/tsh/agent/api/sys_check/health?enm=AgentSysHealthCheckReq
    :return:
    """
    logger.info(f"enm: {enm}")
    response = ApInterfaceVo[AGENT_SYS_HEALTH_CHECK_REP](
        head = generate_head_vo(AGENT_SYS_HEALTH_CHECK_REP),
        body = AGENT_SYS_HEALTH_CHECK_REP(
            status=AgentStatus.ACTIVE,
            version=settings.AP_VERSION,
            path=str(Path(__file__).resolve().parent),
        )
    )
    return response

