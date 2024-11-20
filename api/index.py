from fastapi import FastAPI, Request, Response
from .dbActions import getSession,registerAgent
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

app = FastAPI()
origins = [
    "https://victory-contest.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["victory-contest.vercel.app",]
)
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
