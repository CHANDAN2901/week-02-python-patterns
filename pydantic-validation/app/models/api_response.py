from typing import Any

from pydantic import BaseModel, Field


class APIResponse(BaseModel):
    success: bool = Field(
        ...,
        description="Whether request succeeded",
    )

    message: str = Field(
        ...,
        min_length=3,
    )

    data: Any = Field(
        default=None,
        description="Actual response data",
    )

    errors: list[str] = Field(
        default_factory=list,
    )