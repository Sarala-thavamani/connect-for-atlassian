from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/installed")
async def installed_handler(data: dict):
    return JSONResponse({"message": "App installed successfully"})

@app.get("/hello-world")
async def hello_world():
    return HTMLResponse("""
    <html>
        <head><title>Hello World</title></head>
        <body>
            <h1>Hello, World from FastAPI!</h1>
        </body>
    </html>
    """)
