import logging

from fastapi import APIRouter, Query, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.config.config_manager import ConfigManager
from app.config.sqlite_session import db_helper
from app.controller.common_controller import CommonQueryModel
from app.model.interface.ap_head_vo import generate_head_vo
from app.model.interface.ap_interface_vo import ApInterfaceVo
from app.model.interface.mpms_interface_model import UI_NEW_PLTF_DEF_REQ, UI_NEW_PLTF_DEF_REP, UI_FETCH_PLTF_DEF, \
    UI_NEW_PROD_INF_REQ, UI_NEW_PROD_INF_REP
from app.service.mpms_biz_service import MpmsBizService
from app.util.id_time_util import generate_obj_id

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/mpms",
    tags=["price", "monitor"],
)

settings = ConfigManager()


async def get_mpms_biz_service(db: AsyncSession = Depends(db_helper.get_db)):
    return MpmsBizService(db)


@router.get(UI_FETCH_PLTF_DEF.URI, response_model=ApInterfaceVo[UI_NEW_PLTF_DEF_REP])
async def fetch_platform_definition(
        payload: ApInterfaceVo[UI_FETCH_PLTF_DEF],
        params: CommonQueryModel = Query(),
        service: MpmsBizService = Depends(get_mpms_biz_service),
):
    logger.info(f"payload: {payload}, params: {params}")

    clz = UI_NEW_PLTF_DEF_REP
    response = ApInterfaceVo[clz](
        head=generate_head_vo(clz),
        body=clz(
            siteId=payload.body.siteId,
            userId=payload.body.userId,
            pltfId=generate_obj_id(),
            pltfNm=payload.body.pltfNm,
            pltfAlias=payload.body.pltfAlias,
            pltfBaseUrl=payload.body.pltfBaseUrl,
            retComment="All process is completed",
        )
    )

    return response


@router.post(UI_NEW_PLTF_DEF_REQ.URI, response_model=ApInterfaceVo[UI_NEW_PLTF_DEF_REP])
async def add_new_platform_definition(
        payload: ApInterfaceVo[UI_NEW_PLTF_DEF_REQ],
        params: CommonQueryModel = Query(),
        service: MpmsBizService = Depends(get_mpms_biz_service)):
    logger.info(f"payload: {payload}, params: {params}")

    clz = UI_NEW_PLTF_DEF_REP
    response = ApInterfaceVo[clz](
        head=generate_head_vo(clz),
        body=clz(
            siteId=payload.body.siteId,
            userId=payload.body.userId,
            pltfId=generate_obj_id(),
            pltfNm=payload.body.pltfNm,
            pltfAlias=payload.body.pltfAlias,
            pltfBaseUrl=payload.body.pltfBaseUrl,
            retComment="All process is completed",
        )
    )

    return response


@router.post(UI_NEW_PROD_INF_REQ.URI, response_model=ApInterfaceVo[UI_NEW_PROD_INF_REP])
async def add_new_platform_definition(
        payload: ApInterfaceVo[UI_NEW_PROD_INF_REQ],
        params: CommonQueryModel = Query(),
        service: MpmsBizService = Depends(get_mpms_biz_service)):
    logger.info(f"payload: {payload}, params: {params}")

    clz = UI_NEW_PROD_INF_REP
    response = ApInterfaceVo[clz](
        head=generate_head_vo(clz),
        body=clz(
            siteId=payload.body.siteId,
            userId=payload.body.userId,
            pltfId=generate_obj_id(),
            prodId=generate_obj_id(),
            prodNm=payload.body.prodNm,
            prodBaseUrl=payload.body.prodBaseUrl,
            retComment="All process is completed",
        )
    )

    return response
