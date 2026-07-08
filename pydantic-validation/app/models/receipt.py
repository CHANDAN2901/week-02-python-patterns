from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, Field

class Item(BaseModel):
    name: str = Field(
        ...,
        min_length=2,
        max_length=100,
    )

    quantity: int = Field(
        ...,
        gt=0,
    )

    price: Decimal = Field(
        ...,
        gt=0,
    )


class Receipt(BaseModel):
    store_name: str = Field(
        ...,
        min_length=3,
    )

    purchase_date: datetime

    items: list[Item]

    total: Decimal = Field(
        ...,
        gt=0,
    )