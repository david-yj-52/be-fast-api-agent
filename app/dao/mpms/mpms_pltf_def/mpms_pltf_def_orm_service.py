import logging
import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.mpms.mpms_pltf_def.mpms_pltf_def import AnLclMpmsPltfDef
from app.dao.mpms.mpms_pltf_def.mpms_pltf_def_repository import AnLclMpmsPltfDefRepository
from app.util.id_time_util import generate_id

logger = logging.getLogger(__name__)
class AnLclMpmsPltfDefOrmService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.repo = AnLclMpmsPltfDefRepository(db)

    async def register_platform(self, entity: AnLclMpmsPltfDef):

        try:
            self.repo.save_entity(entity)
            await self.db.flush()

            self.repo.save_history(entity)

            await self.db.commit()
        except Exception as e:
            logger.error(e)
            await self.db.rollback()
            raise e
