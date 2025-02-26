from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def Scraper():
    return {"message": "Scraper API is working!"}
