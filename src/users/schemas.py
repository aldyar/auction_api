from pydantic import BaseModel, Field
class Users(BaseModel):
    tg_id: int
    balance: int = Field(ge = 0)
    name: str = Field(max_length = 32)

    