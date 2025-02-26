from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def job_tracker():
    return {"message": "Job Tracker API is working!"}
