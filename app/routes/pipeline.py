from datetime import datetime

from fastapi import APIRouter
from starlette.responses import Response

router = APIRouter()


@router.get("/pipeline/start_detection", tags=["Pipeline"])
async def start_detection():

    current_time = datetime.utcnow()
    return Response(
        f"Notification API (UTC: {current_time.strftime('%Y.%m.%d %H:%M:%S')})"
    )


@router.get("/pipeline/get_detection_result", tags=["Pipeline"])
async def get_detection_result():

    current_time = datetime.utcnow()
    return Response(
        f"Notification API (UTC: {current_time.strftime('%Y.%m.%d %H:%M:%S')})"
    )
