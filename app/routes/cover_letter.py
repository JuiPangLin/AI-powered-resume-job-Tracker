from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def cover_letter():
    return {"message": "Cover Letter API is working!"}
