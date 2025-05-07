from fastapi import FastAPI # importing fastapi class

app = FastAPI() #creating an instance of the FastAPI class

@app.get("/") # defining a path operation for the root endpoint
def read_root():
    return {"message": "Vanakam da mapla"}
