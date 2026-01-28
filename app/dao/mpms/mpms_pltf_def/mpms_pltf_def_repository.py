from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.cmn.default_model_mixin import UseStatEnum
from app.dao.mpms.mpms_pltf_def.mpms_pltf_def import AnLclMpmsPltfDef, AhLclMpmsPltfDef


class AnLclMpmsPltfDefRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    def save_entity(self, entity: AnLclMpmsPltfDef) -> AnLclMpmsPltfDef:
        self.db.add(entity)
        return entity

    def save_history(self, entity: AnLclMpmsPltfDef) -> AhLclMpmsPltfDef:
        history = entity.to_history()
        self.db.add(history)
        return history

    async def find_all(self, site_id:str, use_state_cd: UseStatEnum) -> Optional[List[AnLclMpmsPltfDef]]:
        stmt = select(AnLclMpmsPltfDef).where(
            AnLclMpmsPltfDef.site_id == site_id,
            AnLclMpmsPltfDef.use_stat_cd == use_state_cd
        )
        result = await self.db.execute(stmt)
        return result.scalar_one_or_none()