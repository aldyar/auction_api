from sqlalchemy import BigInteger, Integer, String, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from core.database import Base

class Order(Base):
    __tablename__ = 'orders'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    uuid: Mapped[str] = mapped_column(String(25), unique=True, nullable=False)  # ID счета Cryptomus
    status: Mapped[str] = mapped_column(String(50), nullable=False)  # Статус платежа
    tg_id: Mapped[int] = mapped_column(BigInteger, nullable=False)  # ID пользователя
    amount: Mapped[str] = mapped_column(String(15), nullable=False)  # Сумма платежа
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    is_processed: Mapped[bool] = mapped_column(Boolean, default=False)  # Обработан ли платеж
    processed_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
