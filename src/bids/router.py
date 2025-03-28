from fastapi import APIRouter, Depends, HTTPException
from src.bids.service import BidService
from sqlalchemy.ext.asyncio import AsyncSession
from src.bids.models import Bid
from src.bids.schemas import BidSchema
from typing import List
from src.core.database import get_session

router = APIRouter()


@router.post("/bids/", response_model=BidSchema)
async def create_bid(bid_data: BidSchema, db: AsyncSession = Depends(get_session)):
    service = BidService(db)
    return await service.create_bid(bid_data)

@router.get("/bids/{bid_id}", response_model=BidSchema)
async def get_bid(bid_id: int, db: AsyncSession = Depends(get_session)):
    service = BidService(db)
    bid = await service.get_bid(bid_id)
    if not bid:
        raise HTTPException(status_code=404, detail="Bid not found")
    return bid

@router.put("/bids/{bid_id}", response_model=BidSchema)
async def update_bid(bid_id: int, bid_data: BidSchema, db: AsyncSession = Depends(get_session)):
    service = BidService(db)
    bid = await service.update_bid(bid_id, bid_data)
    if not bid:
        raise HTTPException(status_code=404, detail="Bid not found")
    return bid

@router.delete("/bids/{bid_id}")
async def delete_bid(bid_id: int, db: AsyncSession = Depends(get_session)):
    service = BidService(db)
    bid = await service.delete_bid(bid_id)
    if not bid:
        raise HTTPException(status_code=404, detail="Bid not found")
    return {"message": "Bid deleted successfully"}

@router.get("/bids/", response_model=List[BidSchema])
async def list_bids(db: AsyncSession = Depends(get_session)):
    service = BidService(db)
    return await service.list_bids()
