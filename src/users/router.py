from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.database import get_session
from src.users.schemas import Users
from src.users.service import UserService

router = APIRouter()

@router.get("/users/{tg_id}", response_model=Users)
def get_user(tg_id: int):
    
    user = UserService.get_user(tg_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/users", response_model=Users)
async def create_user(user:Users, ):
    
    existing_user = await UserService.get_user(user.tg_id)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    return await UserService.create_user(user.tg_id, user.name, user.balance)

@router.put("/users/{tg_id}/balance", response_model=Users)
async def update_balance(tg_id: int, amount: float):
    
    user = await UserService.update_balance(tg_id, amount)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/users/{tg_id}", response_model=dict)
async def delete_user(tg_id: int, ):
    
    success = await UserService.delete_user(tg_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}