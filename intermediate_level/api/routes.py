# This file defines the API routes for the FastAPI application.
# It includes a welcome endpoint and a user creation endpoint.
# The routes are defined using FastAPI's APIRouter class, which allows for modular organization of routes.
# The welcome endpoint returns a simple greeting message.
# The user creation endpoint accepts a UserIn model and returns a UserOut model.
from fastapi import APIRouter
from intermediate_level.models.user import UserOut,UserIn, UserInWithAddress, UserOutWithAddress # importing the UserOut model from models.user
from fastapi import Depends # importing Depends from fastapi
from intermediate_level.services.user_service import get_user_name, get_full_name, get_user_service # importing the get_user_name function from services.user_service

router = APIRouter()

@router.get("/welcome") # defining a path operation for Welcome endpoint
def read_welcome():
    return {"message": "Hi Dude!"}

@router.post("/user", response_model = UserOut)
def create_user(user: UserIn):
    return {"id":1, **user.dict()} # creating a user with id 1 and returning the user data as a dictionary
# The create_user function accepts a UserIn model and returns a UserOut model.

@router.get("/hello") # defining a path operation for Hello endpoint
def read_hello(name: str = Depends(get_user_name)):
    return {"message": f"Hello {name}!"}

@router.post("/user_enroll") # defining a path operation for User Enroll endpoint
def create_user_enroll(user: UserInWithAddress):
    return {"id": 1, **user.dict()}

@router.get("/get_user") # defining a path operation for Get User endpoint
def get_user(name: str = Depends(get_user_name)):
    return {"message": f"Hello {name}!"}
# The get_user function accepts a name parameter and returns a greeting message with the name.

@router.get("/Dependency Injection level 1")
def read_dependency_injection_level_1(name:str =Depends(get_full_name)):
    return {"message": f"Hello {name}!"}

@router.get("/getting user service")
def read_user_service(users: str = Depends(get_user_service)):
    return {"users": f"Hello {users.get_users()}!"}