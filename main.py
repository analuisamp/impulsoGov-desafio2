from fastapi import FastAPI
from datetime import datetime, timezone, timedelta

app = FastAPI()


@app.get("/")
async def root():
    return {"Criando uma API em FastAPI com um endpoint que retorne o horario atual dos fusos horários (-3 GMT) e (GMT – 5)"}

@app.get("/get_time")
async def get_time():
    return {
        "current_time (-3 GMT)": datetime.now(timezone.utc).astimezone(timezone(timedelta(hours=-3))).strftime("%Y-%m-%d %H:%M:%S"),
        "current_time (GMT -5)": datetime.now(timezone.utc).astimezone(timezone(timedelta(hours=-5))).strftime("%Y-%m-%d %H:%M:%S") 
    }

@app.get("/get_especif_time")
async def get_time(gmt: str):
    
    if gmt == "":
        return 
    
    if gmt == "-3":
        return {
            "current_time (-3 GMT)": datetime.now(timezone.utc).astimezone(timezone(timedelta(hours=-3))).strftime("%Y-%m-%d %H:%M:%S")
        }
    elif gmt == "-5":
        return {
            "current_time (GMT -5)": datetime.now(timezone.utc).astimezone(timezone(timedelta(hours=-5))).strftime("%Y-%m-%d %H:%M:%S")
        }
    else:
        return "gmt not found"