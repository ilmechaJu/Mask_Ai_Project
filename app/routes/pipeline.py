import os
import shutil
from datetime import datetime

from fastapi import APIRouter, File, UploadFile
from starlette.responses import Response

from distutils.dir_util import copy_tree

router = APIRouter()


# @app.post("/photo")
# async def upload_photo(file: UploadFile):
#     UPLOAD_DIR = "./photo"  # 이미지를 저장할 서버 경로
    
#     content = await file.read()
#     filename = f{str(uuid.uuid4())}.jpg  # uuid로 유니크한 파일명으로 변경
#     with open(os.path.join(UPLOAD_DIR, filename), "wb") as fp:
#         fp.write(content)  # 서버 로컬 스토리지에 이미지 저장 (쓰기)

#     return {"filename": filename}
    
# # 사진 다운로드 #다운로드는 DB가 필요한듯? (  )
# @app.get("/download/photo/{photo_id}")
# async def download_photo(photo_id: int, db: Session = Depends(get_db)):
#     find_photo: Photo = db.query(Photo).filter_by(photo_id=photo_id).first()
#     return FileResponse(find_photo.src)

BASE_DIR = os.path.abspath(os.path.dirname(__file__)) #현재 실행중인 .py 파일이 있는 경로
IMG_DIR = os.path.join(BASE_DIR, 'images/') #이미지를 저장할 서버 경로


@router.post("/pipeline/start_detection", tags=["Pipeline"])
async def start_detection(image: UploadFile = File(...), image_info: str = ""): #'...'뜻 : import file from Fastapi
    with open(os.path.join(IMG_DIR, f"{image.filename}"), "wb") as buffer: # 파일이름 저장
        shutil.copyfileobj(image.file, buffer) #shutil 뜻 : 파일 저장, 버퍼 메모리
    return {"file_name": image.filename}

@router.get("/pipeline/get_detection_result", tags=["Pipeline"])
async def get_detection_result():

    current_time = datetime.utcnow()
    return Response(
        f"Notification API (UTC: {current_time.strftime('%Y.%m.%d %H:%M:%S')})"
    )
