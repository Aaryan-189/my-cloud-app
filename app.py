from fastapi import FastAPI

app = FastAPI(title="Cloud Deployment Assessment API")

@app.get("/")
def read_root():
    return {"message": "Hello World from Cloud App!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "description": "This is a sample item"}

@app.post("/echo")
def echo_data(data: dict):
    return {"echo": data}