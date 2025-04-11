from fastapi import FastAPI
import uvicorn
from src.core.database import AsyncSessionLocal, get_session
from src.users.router import router as users_router
from src.orders.router import router as orders_router
from src.bids.router import router as bids_router
from dotenv import load_dotenv
import os


load_dotenv()


app = FastAPI(title="Auction API", version="1.0")


app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(orders_router, prefix="/orders", tags=["Orders"])
app.include_router(bids_router, prefix="/bids", tags=["Bids"])


@app.on_event("startup")
async def startup():
    print("🚀 API запущен!")


@app.on_event("shutdown")
async def shutdown():
    await AsyncSessionLocal().close()  
    print("🛑 API остановлен!")

# Тестовый эндпоинт
@app.get("/")
async def root():
    
    return {"message": 'Welcome to auction API v1.0'}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=2000, reload=True)
