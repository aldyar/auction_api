from pydantic import BaseModel, Field
from sqlalchemy import func
from core.database import AsyncSessionLocal
from src.users.schemas import Users
from src.users.models import User
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload

class UserService:
    def connection(func):
    async def inner(*args, **kwargs):
        async with AsyncSessionLocal() as session:
            return await func(session, *args, **kwargs)
    return inner
        

    def get_user(self, tg_id: int) -> Users | None:
        result =  self.session.scalar(select(User).where(User.tg_id==tg_id))
        
        return Users.model_validate(result) if result else None


    
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