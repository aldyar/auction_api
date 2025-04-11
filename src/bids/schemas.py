from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

class BidSchema(BaseModel):
    id: int
    tg_id: Optional[int] = Field(..., description="Telegram ID пользователя",examples=[1075213318])
    request_date: datetime = Field(..., description="Дата запроса",examples=[datetime.now()])
    full_name: str = Field(...,min_length=3, max_length=100, description="Полное имя",examples=['Dean Winchester'])
    phone: str = Field(...,min_length=11, max_length=11, description="Телефон",examples=['79999999999'])
    request_type: str = Field(..., max_length=50, description="Тип запроса",examples=['Тендер'])
    question: str = Field(..., description="Запрос",examples=["Закупка офисной мебели"])
    category: str = Field(..., max_length=100, description="Категория",examples=['тендер'])
    start_price: int = Field(...,gt=0, description="Начальная цена",examples=[1])
    blitz_price: Optional[int] = Field(..., description="текущая-цена")
    valid: bool = Field(default=True, description="Валидность срока действия",examples=[True])



class CreateBids(BaseModel):
    id: int
    # tg_id: Optional[int] = Field(..., description="Telegram ID пользователя",examples=[1075213318])
    request_date: datetime = Field(..., description="Дата запроса",examples=[datetime.now()])
    full_name: str = Field(...,min_length=3, max_length=100, description="Полное имя",examples=['Dean Winchester'])
    phone: str = Field(...,min_length=11, max_length=11, description="Телефон",examples=['79999999999'])
    request_type: str = Field(..., max_length=50, description="Тип запроса",examples=['Тендер'])
    question: str = Field(..., description="Запрос",examples=["Закупка офисной мебели"])
    category: str = Field(..., max_length=100, description="Категория",examples=['тендер'])
    start_price: int = Field(...,gt=0, description="Начальная цена",examples=[1])
    blitz_price: Optional[int] = Field(..., description="текущая-цена")
    #valid: bool = Field(default=True, description="Валидность срока действия",examples=[True])
    



# class BidInvalidSchema(BaseModel):
    
#     tg_id: Optional[int] = Field(..., description="Telegram ID пользователя",examples=[1075213318])
#     request_date: datetime = Field(..., description="Дата запроса",examples=[datetime.now()])
#     full_name: str = Field(...,min_length=3, max_length=100, description="Полное имя",examples=['Dean Winchester'])
#     phone: str = Field(...,min_length=11, max_length=11, description="Телефон",examples=['79999999999'])
#     request_type: str = Field(..., max_length=50, description="Тип запроса",examples=['Тендер'])
#     question: str = Field(..., description="Запрос",examples=["Закупка офисной мебели"])
#     category: str = Field(..., max_length=100, description="Категория",examples=['тендер'])
#     start_price: int = Field(...,gt=0, description="Начальная цена",examples=[1])
#     blitz_price: Optional[int] = Field(..., description="текущая-цена")

class BidInvalidSchema(BaseModel):
    id: int
    tg_id: Optional[int] = Field(None, description="Telegram ID пользователя", examples=[1578213318])
    sold_price: Optional[int] = Field(None, description="Продажная цена", examples=[15000])
    invalid_reason: Optional[str] = Field(None, description="Причина отклонения", examples=["Не указана цена"])
    

