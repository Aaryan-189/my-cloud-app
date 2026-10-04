from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Cloud Deployment Assessment API", version="1.1.0")

# Enable CORS for frontend integration (e.g., a React or Next.js app)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, replace "*" with your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model for strict data validation
class UserData(BaseModel):
    name: str
    project: str

@app.get("/")
def read_root():
    return {"message": "Hello World from Cloud App!"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "version": "1.1.0"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id <= 0:
        raise HTTPException(status_code=400, detail="Item ID must be positive")
    return {"item_id": item_id, "description": "This is a sample item"}

@app.post("/echo")
def echo_data(data: UserData):
    # FastAPI automatically validates that the incoming payload matches the UserData model
    return {"echo": data.model_dump()}