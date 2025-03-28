from typing import List
from src.bids.models import Bid
from src.bids.schemas import BidSchema
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.core.database import AsyncSessionLocal, get_session


class BidService:
    @staticmethod
    async def create_bid(bid_data: BidSchema):
        async with get_session() as session:
            bid = Bid(**bid_data.dict())
            session.add(bid)
            await session.commit()
            await session.refresh(bid)
            return bid

    @staticmethod
    async def get_bid(bid_id: int):
        async with get_session() as session:
            result = await session.execute(select(Bid).filter(Bid.id == bid_id))
            return result.scalar_one_or_none()

    @staticmethod
    async def update_bid(bid_id: int, bid_data: BidSchema):
        async with get_session() as session:
            bid = await BidService.get_bid(bid_id)
            if bid:
                for key, value in bid_data.dict().items():
                    setattr(bid, key, value)
                await session.commit()
                await session.refresh(bid)
            return bid

    @staticmethod
    async def delete_bid(bid_id: int):
        async with get_session() as session:
            bid = await BidService.get_bid(bid_id)
            if bid:
                await session.delete(bid)
                await session.commit()
            return bid

    @staticmethod
    async def list_bids() -> List[Bid]:
        async with get_session() as session:
            result = await session.execute(select(Bid))
            return result.scalars().all()