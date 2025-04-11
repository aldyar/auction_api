from typing import List
from src.bids.models import Bid, BidInvalid
from src.bids.schemas import BidInvalidSchema, BidSchema, CreateBids
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.core.database import AsyncSessionLocal, get_session


class BidService:

    def connection(func):
        async def inner(*args, **kwargs):
            async with AsyncSessionLocal() as session:
                return await func(session, *args, **kwargs)
        return inner
    

    @connection
    async def create_bid(session, bid_data: List[CreateBids]) -> bool:
        bids = [
            Bid(
                id = i.id,
                tg_id=None,
                request_date=i.request_date,
                full_name=i.full_name,
                phone=i.phone,
                request_type=i.request_type,
                question=i.question,
                category=i.category,
                start_price=i.start_price,
                blitz_price=i.blitz_price,
                valid=True,
                bot_taken = 'new'

            )
            for i in bid_data
        ]

        session.add_all(bids)  
        await session.commit()  
        return True  

        

    @connection
    async def fetch_bids(session) -> List[BidSchema] | None:
        result = await session.execute(select(Bid))
        bids = result.scalars().all()




        if bids:

            return [
                BidSchema(
                    id = i.id,
                    tg_id=i.tg_id,
                    request_date=i.request_date,
                    full_name=i.full_name,
                    phone=i.phone,
                    request_type=i.request_type,
                    question=i.question,
                    category=i.category,
                    start_price=i.start_price,
                    blitz_price=i.blitz_price,
                    valid=i.valid
                )
                for i in bids
            ]
        else:
            return None


    @connection
    async def fetch_invalid_bids(session) -> List[BidInvalidSchema] | None:
        result = await session.execute(select(BidInvalid))
        bids = result.scalars().all()
        if bids:

            return [
                BidInvalidSchema(
                    id = i.id,
                    tg_id=i.tg_id,
                    sold_price =i.sold_price,
                    invalid_reason = i.invalid_reason
                )
                for i in bids
            ]
        else:
            return None

    @connection
    async def test(session, bid_data: List[BidSchema] ) -> bool:
        bids = [
            BidInvalid(
                tg_id=i.tg_id,
                request_date=i.request_date,
                full_name=i.full_name,
                phone=i.phone,
                request_type=i.request_type,
                question=i.question,
                category=i.category,
                start_price=i.start_price,
                blitz_price=i.blitz_price,
                
            )
            for i in bid_data
        ]

        session.add_all(bids)  
        await session.commit()  
        return True  


    @connection
    async def get_not_sold_bids(session):
        result = await session.execute(select(Bid.id, Bid.bot_taken).where(Bid.bot_taken == 'not sold'))
        return [{'id': row.id, 'status': row.bot_taken} for row in result.all()]