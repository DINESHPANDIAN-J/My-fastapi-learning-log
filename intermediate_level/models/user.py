# This file defines the User model for the application.
# It uses Pydantic for data validation and serialization.
# The UserIn model is used for input data, while the UserOut model is used for output data.
# The models include fields for username and email, with appropriate types and validation.
# The UserIn model is used for creating new users, while the UserOut model is used for returning user data.
# The models are defined using Pydantic's BaseModel class, which provides built-in validation and serialization features.# This file is part of the intermediate level of the FastAPI tutorial.
from pydantic import BaseModel, EmailStr

class UserIn(BaseModel):
    username: str
    email: EmailStr

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr

