from fastapi import FastAPI
from routes import auth, checkin

app = FastAPI()

app.include_router(auth.router)
app.include_router(checkin.router)

@app.get("/")
def root():
    return {"message": "This is a working FastAPI app"}