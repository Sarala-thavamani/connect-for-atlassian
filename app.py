from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files from a "static" folder
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    print("Root route accessed")
    return HTMLResponse("""
    <html>
        <head><title>FastAPI App</title></head>
        <body>
            <h1>Welcome to the FastAPI Atlassian App</h1>
            <p>Go to <a href="/hello-world">Hello World Page</a></p>
        </body>
    </html>
    """)
    response.headers["X-Frame-Options"] = "ALLOW-FROM https://cn2.atlassian.net/"
    response.headers["Content-Security-Policy"] = "frame-ancestors 'self' https://cn2.atlassian.net/"
    return response
# Lifecycle endpoint to handle app installation
@app.post("/installed")
async def installed_handler(data: dict):
    return JSONResponse({"message": "App installed successfully"})

# Serve the Hello World page
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

# Serve the atlassian-connect.json file
@app.get("/atlassian-connect.json")
async def get_atlassian_connect():
    return StaticFiles(directory="static").get("/atlassian-connect.json")