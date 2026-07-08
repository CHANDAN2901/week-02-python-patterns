from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class UserProfile(BaseModel):
    """
    Represents a user profile in our application.
    """

    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Full name of the user",
        examples=["Chandan Yadav"],
    )

    email: EmailStr = Field(
        ...,
        description="User's email address",
        examples=["chandan@gmail.com"],
    )

    age: int = Field(
        ...,
        ge=18,
        le=100,
        description="Age should be between 18 and 100",
    )

    city: str = Field(
        default="Mumbai",
        description="Current city",
    )

    phone: Optional[str] = Field(
        default=None,
        description="Phone number",
    )

    country: str = Field(
        default="India",
        description="Enter your country"
    )

    is_verified: bool = False

    bio: Optional[str] = Field(
        default=None,
        description="Tell about yourseld"
    )

