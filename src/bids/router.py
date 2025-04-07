from fastapi import APIRouter, Depends, HTTPException
from src.bids.service import BidService
from sqlalchemy.ext.asyncio import AsyncSession
from src.bids.models import Bid
from src.bids.schemas import BidInvalidSchema, BidSchema, CreateBids
from typing import List
from src.core.database import get_session

router = APIRouter()


@router.post("/", response_model=bool)
async def create_bid(bid_data: List[CreateBids]):
    return await BidService.create_bid(bid_data)

@router.post('/create_invalid_bid', response_model=bool)
async def create_invalid_bid(bid_data: List[BidInvalidSchema]):
    return await BidService.test(bid_data)

@router.get("/", response_model=List[BidSchema])
async def fetch_bids():
    bids = await BidService.fetch_bids()
    if bids:
        return bids
    return []
     

@router.get('/invalid_bids', response_model=List[BidInvalidSchema])
async def fetch_invalid_bids():
    bids = await BidService.fetch_invalid_bids()
    if bids:
        return bids
    return []
