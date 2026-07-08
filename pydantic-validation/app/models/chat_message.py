from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


class ChatMessage(BaseModel):
    role: Literal["system", "user", "assistant"] = Field(
        ...,
        description="Role of the message",
    )

    content: str = Field(
        ...,
        min_length=1,
        max_length=5000,
        description="Message content",
    )

    token_count: int = Field(
        default=0,
        ge=0,
        description="Estimated number of tokens",
    )

    created_at: datetime = Field(
        default_factory=datetime.now,
    )