from sqlalchemy import BigInteger, Float, String
from sqlalchemy.orm import Mapped, mapped_column
from src.core.database import Base

class User(Base):
    __tablename__ = 'users'
    
    tg_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    balance: Mapped[float] = mapped_column(Float, default=0)
    name: Mapped[str] = mapped_column(String(32))
