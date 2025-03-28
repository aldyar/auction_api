import os
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from contextlib import asynccontextmanager
from dotenv import load_dotenv

# Загружаем переменные окружения из .env
load_dotenv()

# Берем DATABASE_URL из .env
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL не найден в .env!")

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = async_sessionmaker(engine)

@asynccontextmanager
async def get_session():
    session: AsyncSession = async_session()
    try:
        yield session
    finally:
        await session.close()

class Base(AsyncAttrs, DeclarativeBase):
    pass
