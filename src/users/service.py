from pydantic import BaseModel, Field
from src.users.schemas import Users
from src.users.models import User
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload

class UserService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_user(self, tg_id: int) -> Users | None:
        result = await self.session.execute(select(User).filter_by(tg_id=tg_id))
        user = result.scalars().first()
        return Users.model_validate(user) if user else None
    
    async def create_user(self, users:Users) -> Users:
        user = User(tg_id=users.tg_id, name=users.name, balance=users.balance)
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return Users.model_validate(user)

    async def update_balance(self, tg_id: int, amount: float) -> Users | None:
        user = await self.get_user(tg_id)
        if user:
            db_user = await self.session.get(User, tg_id)
            db_user.balance += amount
            await self.session.commit()
            await self.session.refresh(db_user)
            return Users.model_validate(db_user)
        return None

    async def delete_user(self, tg_id: int) -> bool:
        user = await self.session.get(User, tg_id)
        if user:
            await self.session.delete(user)
            await self.session.commit()
            return True
        return False