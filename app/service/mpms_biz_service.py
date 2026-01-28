from sqlalchemy.ext.asyncio import AsyncSession


class MpmsBizService:

    def __init__(self, db: AsyncSession):
        self.db = db

    pass
