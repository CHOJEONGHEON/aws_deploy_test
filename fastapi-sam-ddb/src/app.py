from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/health")
def health_check():
    return {"ok": True}

handler = Mangum(app)
