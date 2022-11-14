from datetime import datetime

from fastapi import APIRouter
from starlette.responses import Response

router = APIRouter()

@router.get("/")
async def index():
    """
    ELB 상태 체크용 API
    :return:
    """
    user = Users(status='activate', name="Hellollo")
    session.add(user)
    session.commit()

    Users().create(session, auto_commit=True, name= "코알라")
    current_time = datetime.utcnow()
    return Response(f"Notification API (UTC: {current_time.strftime('%Y.%m.%d %H:%M:%S')})")
