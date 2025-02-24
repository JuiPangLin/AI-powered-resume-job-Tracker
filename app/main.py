from fastapi import FastAPI
from app.routes import resume, cover_letter, job_tracker, scraper

app = FastAPI()

# Include API routes
app.include_router(resume.router, prefix="/resume", tags=["Resume Analysis"])
app.include_router(cover_letter.router, prefix="/cover_letter", tags=["Cover Letter Generation"])
app.include_router(job_tracker.router, prefix="/job_tracker", tags=["Job Tracking"])
app.include_router(scraper.router, prefix="/scraper", tags=["Web Scraping"])

@app.get("/")
def root():
    return {"message": "AI-Powered Resume & Job Tracker API"}
