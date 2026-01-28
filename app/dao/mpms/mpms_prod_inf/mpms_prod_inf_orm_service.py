import logging
from typing import Optional

from sqlalchemy import Sequence
from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.cmn.default_model_mixin import UseStatEnum
from app.dao.mpms.mpms_prod_inf.mpms_prod_inf import AnLclMpmsProdInf
from app.dao.mpms.mpms_prod_inf.mpms_prod_inf_repository import AnLclMpmsProdInfRepository

logger = logging.getLogger(__name__)
class AnLclMpmsProdInfOrmService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.repo = AnLclMpmsProdInfRepository(db)

    async def register_product_info(self, entity: AnLclMpmsProdInf):

        try:
            self.repo.save_entity(entity)
            await self.db.flush()

            self.repo.save_history(entity)

            await self.db.commit()
        except Exception as e:
            logger.error(e)
            await self.db.rollback()
            raise e

    async def fetch_product_info(self, site_id: str, pltf_id:str, prod_id:str)-> Optional[Sequence[AnLclMpmsProdInf]]:
        return self.repo.find_pltf_and_prod(site_id, pltf_id, prod_id, UseStatEnum.USABLE)