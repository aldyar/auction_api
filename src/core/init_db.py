from core.database import engine, async_session
from users.models import User
from bids.models import Bid
from orders.models import Order

async def init_db():
    async with engine.begin() as conn:
       
        pass  
