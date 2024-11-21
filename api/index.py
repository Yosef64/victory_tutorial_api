import os
from fastapi import FastAPI, Request, Response
import requests
from fastapi.responses import JSONResponse
from .dbActions import getSession, getUser,registerAgent
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
TOKEN = os.getenv("BOT_TOKEN")

app = FastAPI()
origins = [
    "https://victory-contest.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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
@app.post("/check_user")
async def check_user(request:Request):
    data = await request.json()
    try:
        ref = getUser(data["teleid"])
        return {"message": len(ref) == 0}
    except Exception as e:
        return {"message":e}
@app.post("/sendMessage")
async def send_message(request:Request):
    data = await request.json()
    CHAT_ID ,text = data["chat_id"] , "You are already regitered!"
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": text}
        response = requests.post(url, json=payload)
        return JSONResponse({"message":"ok"},status_code=200)
    except Exception as e:
        return JSONResponse({"message":e},status_code=500)
         
@app.get("/")
async def index(request:Request):
    return {"message":"ok"}

#https://api.telegram.org/bot7756252447:AAH6fSVh8Q6s2hip4w4wCblqDuOtrLSWSR4/sendMessage?chat_id=1656463485&text=hebabe