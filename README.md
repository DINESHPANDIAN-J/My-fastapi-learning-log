"# My-fastapi-learning-log" 

# FastAPI - Vanakam da mapla

## Run Locally
- pip install -r requirements.txt
- uvicorn main:app --reload

## intermediate_level 
# Lesson 1: | app/api/routes.py
- Organize with API Router
- Goal: Learn to seperate your routes for scalability.
# Lesson 2: | app/models/user.py
- Use Pydantic Models for Requests & Responses:
# Lesson 3: | 
- '''Dependency Injection is a design pattern where objects (dependencies) are passed into functions or classes rather than being created inside them. In FastAPI, DI is built-in and beautifully simple using Depends.
'''
- Dependency Injection allows you to:
- Reuse logic across endpoints
- Keep routes clean and focused
- Inject things like DB sessions, auth logic, or service classes
- Make testing easier with mockable input

# Lesson:4 Global Exception & Error Handling in FastAPI
- Real-world APIs break. When they do, clear and consistent error handling is critical. FastAPI makes it easy to:

- Catch specific exceptions (e.g., HTTPException, ValueError)

- Return custom error messages

- Format error responses in a standardized way

- Handle unexpected crashes gracefully