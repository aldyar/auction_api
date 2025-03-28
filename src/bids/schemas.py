from datetime import datetime
from pydantic import BaseModel, Field

class BidSchema(BaseModel):
    id: int
    tg_id: int = Field(..., description="Telegram ID пользователя")
    request_date: datetime = Field(..., description="Дата запроса")
    full_name: str = Field(..., max_length=255, description="Полное имя")
    phone: str = Field(..., max_length=20, description="Телефон")
    request_type: str = Field(..., max_length=50, description="Тип запроса")
    question: str = Field(..., description="Запрос")
    category: str = Field(..., max_length=100, description="Категория")
    start_price: int = Field(..., description="Начальная цена")
    blitz_price: int = Field(..., description="текущая-цена")
    valid: bool = Field(default=True, description="Валидность срока действия")

    class Config:
        orm_mode = True