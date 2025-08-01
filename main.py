from fastapi import FastAPI
from app.routes import pickups, users, auth, payments, reports
from app.database.models import Base
from app.database.db import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(pickups.router)
app.include_router(reports.router)
app.include_router(payments.router)

@app.get("/")
def root():
    return {"message": "Waste Management API is running"}
