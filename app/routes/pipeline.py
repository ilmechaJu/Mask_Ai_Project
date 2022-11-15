import os
import shutil
from datetime import datetime

from fastapi import APIRouter, File, UploadFile
from starlette.responses import Response

router = APIRouter()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
IMG_DIR = os.path.join(BASE_DIR, 'images/')
SERVER_IMG_DIR = os.path.join('http://localhost:8000/','images/')

@router.post("/pipeline/start_detection", tags=["Pipeline"])
async def start_detection(image: UploadFile = File(...), image_info: str = ""):
    with open(f"{image.filename}", "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)
    IMG_DIR
    SERVER_IMG_DIR
    return {"file_name": image.filename}


@router.get("/pipeline/get_detection_result", tags=["Pipeline"])
async def get_detection_result():

    current_time = datetime.utcnow()
    return Response(
        f"Notification API (UTC: {current_time.strftime('%Y.%m.%d %H:%M:%S')})"
    )
