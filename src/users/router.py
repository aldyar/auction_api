from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.database import get_session
from src.users.schemas import Users
from src.users.service import UserService

router = APIRouter()

