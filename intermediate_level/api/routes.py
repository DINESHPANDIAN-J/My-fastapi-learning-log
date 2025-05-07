from fastapi import APIRouter

router = APIRouter()

@router.get("/welcome") # defining a path operation for Welcome endpoint
def read_welcome():
    return {"message": "Hi Dude!"}