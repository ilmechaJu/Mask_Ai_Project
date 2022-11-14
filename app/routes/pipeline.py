import shutil
from datetime import datetime

from fastapi import UploadFile, File
from fastapi import APIRouter
from starlette.responses import Response

router = APIRouter()


@router.post("/pipeline/start_detection", tags=["Pipeline"])
async def start_detection(image: UploadFile = File(...), image_info: str = ""):
    with open(f"{image.filename}", "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)
    return {"file_name": image.filename}


@router.get("/pipeline/get_detection_result", tags=["Pipeline"])
async def get_detection_result():

    current_time = datetime.utcnow()
    return Response(
        f"Notification API (UTC: {current_time.strftime('%Y.%m.%d %H:%M:%S')})"
    )
