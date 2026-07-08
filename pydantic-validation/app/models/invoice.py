from datetime import datetime
from decimal import Decimal
from enum import Enum
from uuid import UUID, uuid4

from pydantic import BaseModel, EmailStr, Field

class InvoiceStatus(str, Enum):
    PENDING = "pending"
    PAID = "paid"
    CANCELLED = "cancelled"


class Invoice(BaseModel):
    invoice_id: UUID = Field(
        default_factory=uuid4,
        description="Unique invoice identifier",
    )

    customer_name: str = Field(
        ...,
        min_length=3,
        max_length=100,
    )

    customer_email: EmailStr

    amount: Decimal = Field(
        ...,
        gt=0,
    )

    issued_at: datetime = Field(
        default_factory=datetime.now,
    )

    status: InvoiceStatus = InvoiceStatus.PENDING