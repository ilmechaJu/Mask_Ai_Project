from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import Response

from app.database.conn import db
from app.database.schema import Users
from datetime import datetime


router = APIRouter()


@router.get("/")
async def index(session: Session = Depends(db.session),):
    """
    ELB 상태 체크용 API
    :return:
    """
    
    Users().create(Session, auto_commit=True, name= "코알라")
    current_time = datetime.utcnow()
    return Response(
        f"Notification API (UTC: {current_time.strftime('%Y.%m.%d %H:%M:%S')})"
    )
