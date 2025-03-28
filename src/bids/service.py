from typing import List
from src.bids.models import Bid
from src.bids.schemas import BidSchema

class BidService:
    def __init__(self, session):
        self.session = session

    def create_bid(self, bid_data: BidSchema):
        bid = Bid(**bid_data.dict())
        self.session.add(bid)
        self.session.commit()
        self.session.refresh(bid)
        return bid

    def get_bid(self, bid_id: int):
        return self.session.query(Bid).filter(Bid.id == bid_id).first()

    def update_bid(self, bid_id: int, bid_data: BidSchema):
        bid = self.get_bid(bid_id)
        if bid:
            for key, value in bid_data.dict().items():
                setattr(bid, key, value)
            self.session.commit()
            self.session.refresh(bid)
        return bid

    def delete_bid(self, bid_id: int):
        bid = self.get_bid(bid_id)
        if bid:
            self.session.delete(bid)
            self.session.commit()
        return bid

    def list_bids(self) -> List[BidSchema]:
        return self.session.query(Bid).all()