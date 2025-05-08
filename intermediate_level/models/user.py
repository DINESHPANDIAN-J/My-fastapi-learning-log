# This file defines the User model for the application.
# It uses Pydantic for data validation and serialization.
# The UserIn model is used for input data, while the UserOut model is used for output data.
# The models include fields for username and email, with appropriate types and validation.
# The UserIn model is used for creating new users, while the UserOut model is used for returning user data.
# The models are defined using Pydantic's BaseModel class, which provides built-in validation and serialization features.# This file is part of the intermediate level of the FastAPI tutorial.


#----------Lesson 1: User Model----------
# from pydantic import BaseModel, EmailStr
# class UserIn(BaseModel):
#     username: str
#     email: EmailStr

# class UserOut(BaseModel):
#     id: int
#     username: str
#     email: EmailStr

#Lesson 2: User Model with Optional Fields
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
class UserIn(BaseModel):
    name : str = Field(..., title="Name of the user",min_length=3, max_length=50, example="Vetrivel Murugan")
    email: EmailStr = Field(..., title="Email of the user", example="arohara@gmail.com")
    age: int =Field(..., title="Age of the user", ge=18, le=120, example=25)
    whatsapp_no: Optional[str] = None

class UserOut(BaseModel):
    id: int =Field(..., title="ID of the User", example=1)
    name: str = Field(..., title="Name of the User", example="Vetrivel Murugan")
    email: EmailStr = Field(..., title="Email of the User", example="arohara@gmail.com")
    age: int =Field(..., title="Age of the User", example=25)
    whatsapp_no: Optional[str] = None

# Lesson 3: implementing Nested Models
from intermediate_level.models.common import Address
class Address(BaseModel):
    street: str = Field(..., title="Street of the user", example="123 Main St")
    city: str = Field(..., title="City of the user", example="Chennai")
    state: str = Field(..., title="State of the user", example="Tamil Nadu")
    country: str = Field(..., title="Country of the user", example="India")
    zip_code: str = Field(..., title="Zip code of the user", example="600001")

class UserInWithAddress(BaseModel):
    name : str = Field(..., title="Name of the user",min_length=3, max_length=50, example="Vetrivel Murugan")
    email: EmailStr = Field(..., title="Email of the user", example="123@gmail.com")
    age: int =Field(..., title="Age of the user", ge=18, le=120, example=25)
    whatsapp_no: Optional[str] = None  # Optional field for WhatsApp number
    address: Address # Nested model for address.  

class UserOutWithAddress(BaseModel):
    id: int =Field(..., title="ID of the User", example=1)
    name: str = Field(..., title="Name of the User", example="Vetrivel Murugan")
    email: EmailStr = Field(..., title="Email of the User", example="abc@gmail.com")
    age: int =Field(..., title="Age of the User", example=25)
    whatsapp_no: Optional[str] = None  # Optional field for WhatsApp number
    address: Address # Nested model for address.
