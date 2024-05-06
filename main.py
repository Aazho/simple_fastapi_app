from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Create an instance of FastAPI
app = FastAPI()

class User(BaseModel):
    username: str

# Define a route handler for the root URL
@app.get("/")
def read_root():
    # Return "Hello, World!" as a response
    return {"message": "Hello, World!"}

@app.post("/post-example/")
def post_example(username: User):
    # Perform any necessary validation on the username parameter
    if not username:
        raise HTTPException(status_code=400, detail="Username cannot be empty")
    
    # Return a simple message with status code 200
    return {"message": f"Received username: {username}"}