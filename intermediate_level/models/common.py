# Lesson 3: implementing Nested Models
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
class Address(BaseModel):
    street: str = Field(..., title="Street of the user", example="123 Main St")
    city: str = Field(..., title="City of the user", example="Chennai")
    state: str = Field(..., title="State of the user", example="Tamil Nadu")
    country: str = Field(..., title="Country of the user", example="India")
    zip_code: str = Field(..., title="Zip code of the user", example="600001")