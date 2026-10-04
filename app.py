from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI(title="Cloud Deployment Assessment API", version="1.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    return {"echo": data.model_dump()}

# --- NEW UI ENDPOINT ---
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cloud Microservice UI</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-slate-900 flex items-center justify-center h-screen text-slate-200">
    <div class="bg-slate-800 p-8 rounded-xl shadow-2xl w-full max-w-lg border border-slate-700">
        <h1 class="text-3xl font-bold mb-2 text-white">Cloud API Dashboard</h1>
        <p class="text-slate-400 mb-8">Interact with the deployed microservice.</p>
        
        <div class="space-y-4">
            <button onclick="fetchData('/health')" class="w-full bg-blue-600 hover:bg-blue-500 text-white font-semibold py-3 px-4 rounded-lg transition-colors">
                Check System Health (GET)
            </button>
            <button onclick="fetchData('/items/42')" class="w-full bg-emerald-600 hover:bg-emerald-500 text-white font-semibold py-3 px-4 rounded-lg transition-colors">
                Fetch Item 42 (GET)
            </button>
            <button onclick="postData()" class="w-full bg-indigo-600 hover:bg-indigo-500 text-white font-semibold py-3 px-4 rounded-lg transition-colors">
                Test Data Payload (POST)
            </button>
        </div>

        <div class="mt-8">
            <h2 class="text-xs font-bold text-slate-500 uppercase tracking-widest mb-2">Server Response</h2>
            <pre id="response-box" class="bg-slate-950 text-emerald-400 p-4 rounded-lg text-sm overflow-x-auto h-40 border border-slate-800">Awaiting action...</pre>
        </div>
    </div>

    <script>
        async function fetchData(endpoint) {
            try {
                const response = await fetch(endpoint);
                const data = await response.json();
                document.getElementById('response-box').innerText = JSON.stringify(data, null, 2);
            } catch (error) {
                document.getElementById('response-box').innerText = "Error fetching data.";
            }
        }

        async function postData() {
            try {
                const response = await fetch('/echo', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ name: "Aaryan", project: "Live Dashboard" })
                });
                const data = await response.json();
                document.getElementById('response-box').innerText = JSON.stringify(data, null, 2);
            } catch (error) {
                document.getElementById('response-box').innerText = "Error posting data.";
            }
        }
    </script>
</body>
</html>
"""

@app.get("/ui", response_class=HTMLResponse)
def get_ui():
    return html_content