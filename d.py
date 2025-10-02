# src/app.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health_check():
    return {"ok": True}

try:
    from mangum import Mangum  # 설치되어 있지 않으면 ImportError
    handler = Mangum(app)
except Exception:
    handler = None
