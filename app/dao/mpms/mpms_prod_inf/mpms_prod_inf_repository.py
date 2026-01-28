from typing import List, Optional

from sqlalchemy import select, Sequence
from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.cmn.default_model_mixin import UseStatEnum
from app.dao.mpms.mpms_prod_inf.mpms_prod_inf import AnLclMpmsProdInf, AhLclMpmsProdInf


class AnLclMpmsProdInfRepository():
    def __init__(self, db: AsyncSession):
        self.db = db

    def save_entity(self, entity: AnLclMpmsProdInf) -> AnLclMpmsProdInf:
        self.db.add(entity)
        return entity

    def save_history(self, entity: AnLclMpmsProdInf) -> AhLclMpmsProdInf:
        history = entity.to_history()
        self.db.add(history)
        return history

    async def find_pltf_and_prod(self, site_id: str, pltf_id:str, prod_id:str, use_stat_cd: UseStatEnum) -> Optional[Sequence[AnLclMpmsProdInf]]:
        stmt = select(AnLclMpmsProdInf).where(
            AnLclMpmsProdInf.site_id == site_id,
            AnLclMpmsProdInf.pltf_id == pltf_id,
            AnLclMpmsProdInf.prod_id == prod_id,
            AnLclMpmsProdInf.use_stat_cd == use_stat_cd
        )
        result = await self.db.execute(stmt)
        return result.scalars().all()

    async def find_all(self, site_id:str, use_state_cd: UseStatEnum) -> Optional[Sequence[AnLclMpmsProdInf]]:
        stmt = select(AnLclMpmsProdInf).where(
            AnLclMpmsProdInf.site_id == site_id,
            AnLclMpmsProdInf.use_stat_cd == use_state_cd
        )
        result = await self.db.execute(stmt)
        return result.scalars().all()