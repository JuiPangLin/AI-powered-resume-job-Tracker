from fastapi import FastAPI
from app.routes import resume



app = FastAPI()
app.include_router(resume.router, prefix="/resume", tags=["Resume Analysis"])

@app.get("/")
def root():
    return {"message": "AI-Powered Resume & Job Tracker API"}
