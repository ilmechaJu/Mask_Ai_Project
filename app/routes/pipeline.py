import os
import shutil
from datetime import datetime

from fastapi import APIRouter, File, UploadFile
from starlette.responses import Response

from distutils.dir_util import copy_tree

router = APIRouter()

    

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
IMG_DIR = os.path.join(BASE_DIR, 'images/') 


@router.post("/pipeline/start_detection", tags=["Pipeline"])
async def start_detection(image: UploadFile = File(...), image_info: str = ""): 
    with open(os.path.join(IMG_DIR, f"{image.filename}"), "wb") as buffer:
        shutil.copyfileobj(image.file, buffer) 
    return {"file_name": image.filename}



# # 사진 다운로드 #다운로드는 DB가 필요한듯? (  )
# @app.get("/download/photo/{photo_id}")
# async def download_photo(photo_id: int, db: Session = Depends(get_db)):
#     find_photo: Photo = db.query(Photo).filter_by(photo_id=photo_id).first()
#     return FileResponse(find_photo.src)




@router.get("/pipeline/get_detection_result", tags=["Pipeline"])
async def get_detection_result():

    current_time = datetime.utcnow()
    return Response(
        f"Notification API (UTC: {current_time.strftime('%Y.%m.%d %H:%M:%S')})"
    )
