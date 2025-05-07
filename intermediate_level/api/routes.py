# This file defines the API routes for the FastAPI application.
# It includes a welcome endpoint and a user creation endpoint.
# The routes are defined using FastAPI's APIRouter class, which allows for modular organization of routes.
# The welcome endpoint returns a simple greeting message.
# The user creation endpoint accepts a UserIn model and returns a UserOut model.
from fastapi import APIRouter
from intermediate_level.models.user import UserOut,UserIn # importing the UserOut model from models.user

router = APIRouter()

@router.get("/welcome") # defining a path operation for Welcome endpoint
def read_welcome():
    return {"message": "Hi Dude!"}

@router.post("/user", response_model = UserOut)
def create_user(user: UserIn):
    return {"id":1, **user.dict()}