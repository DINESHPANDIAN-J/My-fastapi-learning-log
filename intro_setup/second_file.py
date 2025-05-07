from fastapi import FastAPI

app = FastAPI()

@app.get("/home") # edefining a path operation for home endpoint
def read_home():
    return {"message": "vakam da mapla home la irunthu!"}

app.get("/about") # defining a path operation for about endpoint
def read_about():
    return {"message_1": "vakam da mapla about la irunthu!", "message_2": "Nan tha Dinesh J!"}