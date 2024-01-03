from fastapi import APIRouter
from app.models import PhotoRequest


router = APIRouter()

@router.post("/upload-photo/")
async def upload_photo(photo_request: PhotoRequest):
    #until model is ready
    return {"message": "done", "photo_path": photo_request.photo_path}


@router.get("/")
async def main():
    return "Welcome to the NSFW Detector API, visit http://127.0.0.1:8000/docs to view all endpoints"
