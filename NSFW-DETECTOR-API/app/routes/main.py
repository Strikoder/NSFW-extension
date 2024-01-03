from fastapi import APIRouter, Request
from app.models import PhotoRequest


router = APIRouter()

@router.post("/upload-photo/")
async def upload_photo(photo_request: PhotoRequest):
    #until model is ready
    return {"message": "done", "photo_path": photo_request.photo_path}


@router.get("/")
async def main(request: Request):
    base_url = request.base_url
    return f"Welcome to the NSFW Detector API, visit {base_url}docs to view all endpoints"
