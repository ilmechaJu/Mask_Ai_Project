from datetime import datetime, timedelta

import bcrypt
import jwt
from fastapi import APIRouter, Depends

# TODO:
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from app.common.consts import JWT_SECRET, JWT_ALGORITHM
from app.database.conn import db
# from app.database.schema import Users
from common.models import ImageInfo, DetectionResult

"""
1. 구글 로그인을 위한 구글 앱 준비 (구글 개발자 도구)
2. FB 로그인을 위한 FB 앱 준비 (FB 개발자 도구)
3. 카카오 로그인을 위한 카카오 앱준비( 카카오 개발자 도구)
4. 이메일, 비밀번호로 가입 (v)
5. 가입된 이메일, 비밀번호로 로그인, (v)
6. JWT 발급 (v)

7. 이메일 인증 실패시 이메일 변경
8. 이메일 인증 메일 발송
9. 각 SNS 에서 Unlink 
10. 회원 탈퇴
11. 탈퇴 회원 정보 저장 기간 동안 보유(법적 최대 한도차 내에서, 가입 때 약관 동의 받아야 함, 재가입 방지 용도로 사용하면 가능)
"""


router = APIRouter()


# route 설계
# - input : 이미지
# - output : bounding box(x, y, w, h), classification_mask_on/off (bool)
# - method
# -- CRUD API : post
# -- 비동기 프로그래밍

# like this---

# @router.post("/mask_tool/detect/get_result", status_code=200)
# async def get_detection_result(client_id : str, image : bytes, image_info: ImageInfo):
#     bounding_box_info, classification_mask_onoff = process(image)
#     return DetectionResult(bounding_box_info, classification_mask_onoff)

# @router.post("/input/", status_code=200)
# async def input(input_type: InputType, reg_info: ...):
#     if input == InputType.image:
#         is_exist = await is_image_exist(reg_info.image)
#         if not reg_info.image:
#             return JSONResponse(status_code=400, content=dict(msg="Image must be provided'"))
#         if is_exist:
#             return JSONResponse(status_code=400, content=dict(msg="Image_EXISTS"))

# async def is_image_exist(image: jpg):
#     get_image = Users.get(image=image) 
#     if get_image:
#         return True
#     return False
   
    

# @router.post("/output/", status_code=200)
# async def input(input_type: OutputType, reg_info: ...):
#     if input == OutputType.image:
#         is_exist = await is_image_exist(reg_info.image)
#         if not reg_info.image:
#             return JSONResponse(status_code=400, content=dict(msg="Image must be provided'"))
#         if is_exist:
#             return JSONResponse(status_code=400, content=dict(msg="Image_EXISTS"))

# def process(image):
#     return 

