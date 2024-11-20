from fastapi import FastAPI, Request, Response
from .dbActions import getSession,registerAgent
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware


# origins = [
#     "https://victory-contest.vercel.app/",
# ]
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   
    allow_methods=["*"],  
    allow_headers=["*"],
)
@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    print(f"Response: {response.status_code}")
    return response
@app.post("/register")
async def agentRegister(request:Request):
    
    data = await request.json()
    referal = getSession(data["teleid"])
    try:
        registerAgent(data,referal)
        return {"message":"ok"}
    except Exception as e:
        return {"message": str(e), "status_code": 500}
@app.get("/")
async def index(request:Request):
    return {"message":"ok"}
