import os
import shutil
import uuid
from datetime import datetime

from fastapi import FastAPI, APIRouter, File, UploadFile, Depends
from sqlalchemy.orm import Session
from starlette.responses import Response, FileResponse

from distutils.dir_util import copy_tree
from app.database.schema import Images
from app.database.conn import db
router = APIRouter()

    
#현재 폴더경로 주소
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
IMG_DIR = os.path.join(BASE_DIR, 'images/') 

#이미지 업로드
@router.post("/pipeline/start_detection", tags=["Pipeline"])
async def start_detection(image: UploadFile = File(...), image_info: str = "", db: Session = Depends(db.get_db)): 
    photo_id = str(uuid.uuid4())
    img_name, extention = image.filename.split(".")
    ufile_name = os.path.join(IMG_DIR, f"{img_name}_{photo_id}.{extention}")
    with open(ufile_name, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer) 
    Images.create(db, photo_id=photo_id, file_path = ufile_name, created_at=datetime.now())
    return {"file_name": image.filename, "photo_id": photo_id}

# # 이미지 업로드 2
# @router.post("/photo")
# async def upload_photo(file: UploadFile):
#     UPLOAD_DIR = "./photo"  # 이미지를 저장할 서버 경로
    
#     content = await file.read()
#     filename = f"{str(uuid.uuid4())}.jpg"  # uuid로 유니크한 파일명으로 변경
#     with open(os.path.join(UPLOAD_DIR, filename), "wb") as fp:
#         fp.write(content)  # 서버 로컬 스토리지에 이미지 저장 (쓰기)

#     return {"filename": filename}



#이미지 다운로드
@router.get("/download/photo/{photo_id}", tags=["Test"])
async def download_photo(photo_id: int):
    # find_photo: Photo = db.query(Photo).filter_by(photo_id=photo_id).first()
    return FileResponse("app/routes/images/beach.jpg")




@router.get("/pipeline/get_detection_result", tags=["Pipeline"])
async def get_detection_result():

    current_time = datetime.utcnow()
    return Response(
        f"Notification API (UTC: {current_time.strftime('%Y.%m.%d %H:%M:%S')})"
    )
