from sqlalchemy import BigInteger, Date, Integer, String, DateTime, Boolean, Text
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from src.core.database import Base

class Bid(Base):
    __tablename__ = 'bids'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    tg_id: Mapped[int] = mapped_column(BigInteger, nullable=True)
    request_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    full_name: Mapped[str] = mapped_column(String(255), nullable=False)
    phone: Mapped[str] = mapped_column(String(20), nullable=False)
    request_type: Mapped[str] = mapped_column(String(50), nullable=False)
    question: Mapped[str] = mapped_column(Text, nullable=False)
    category: Mapped[str] = mapped_column(String(100), nullable=False)
    start_price: Mapped[int] = mapped_column(Integer, nullable=False)
    blitz_price: Mapped[int] = mapped_column(Integer, nullable=True)
    valid: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    bot_taken: Mapped[str] = mapped_column(String(20), nullable=True)


class BidInvalid(Base):
    __tablename__ = 'bids_invalid'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    tg_id: Mapped[int] = mapped_column(BigInteger, nullable=True)
    request_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    full_name: Mapped[str] = mapped_column(String(255), nullable=False)
    phone: Mapped[str] = mapped_column(String(20), nullable=False)
    request_type: Mapped[str] = mapped_column(String(50), nullable=False)
    question: Mapped[str] = mapped_column(Text, nullable=False)
    category: Mapped[str] = mapped_column(String(100), nullable=False)
    start_price: Mapped[int] = mapped_column(Integer, nullable=False)
    blitz_price: Mapped[int] = mapped_column(Integer, nullable=True)


# class ActiveBids(Base):
#     __tablename__ = 'bids_invalid'

#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     bid_id: Mapped[int] = mapped_column(Integer, nullable=False)
#     tg_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
#     current_price: Mapped[int] = mapped_column(BigInteger, nullable=True)
#     start_price: Mapped[int] = mapped_column(BigInteger, nullable=False)
#     blitz_price:   Mapped[int] = mapped_column(BigInteger, nullable=True)
#     created_at: Mapped[datetime] = mapped_column(Date, nullable=False)
#     updated_at: Mapped[datetime] = mapped_column(Date, nullable=True)
