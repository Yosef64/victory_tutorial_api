from fastapi import FastAPI, Request, Response
from .dbActions import getSession,registerAgent
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,  
    allow_methods=["*"],  
    allow_headers=["*"],
)
@app.post("/register")
async def agentRegister(request:Request):
    
    data = await request.json()
    referal = getSession(data["tele_id"])
    try:
        registerAgent(data,referal)
        return Response({{"message":"ok"}},status_code=200)
    except Exception as e:
        return Response({"message":e},status_code=500)
@app.get("/")
async def index(request:Request):
    return Response({"message":"ok"},status_code=200)