
from nanoid import generate
from .db import db
from datetime import datetime
userInfo_ref = db.collection("Agents").document("agentInfo")
userStat_ref = db.collection("Agents").document("agentStat")
payment_ref = db.collection("paymentReq")
session_ref = db.collection("session")

def registerAgent(userInfo,referal):
    agentStat = {"ownStud":0,"agentStud":0,"parent":str(referal),"timestamp":[],"totalAmount":0}
    userReferal = generate(size=10)
    userInfo_ref.update({userReferal:userInfo})
    userStat_ref.update({userReferal:agentStat})


def addSession(tele_id,referal):
    ref = session_ref.document(tele_id)
    if ref.get().exists:
        return
    ref.set({"referal":referal})
    
def getSession(tele_id):
    ref = session_ref.document(tele_id).get()
    if ref.exists:
        data = ref.to_dict()
        return data["referal"]
    return ""

def getUser(tele_id):
    agent_info = userInfo_ref.get().to_dict()
    ref = ""
    for key in agent_info:
        if agent_info[key]["teleid"] == tele_id:
            ref = key
            break
    return ref
    

    
    
