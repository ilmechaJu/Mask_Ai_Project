from enum import Enum

from pydantic import BaseModel

class ImageInfo(BaseModel):
    image_size_with: int
    image_size_height: int


class DetectionResult :
    bounding_box_info : bounding_box_info
    classification_mask_onoff : bool


class bounding_box_info :
    "x" : int
    "y" : int
    "width" : int
    "height" : int





"""class UserRegister(BaseModel):
    # pip install 'pydantic[email]'
    email: EmailStr = None
    pw: str = None


class SnsType(str, Enum):
    email: str = "email"
    facebook: str = "facebook"
    google: str = "google"
    kakao: str = "kakao"


class Token(BaseModel):
    Authorization: str = None


class UserToken(BaseModel):
    id: int
    pw: str = None
    email: str = None
    name: str = None
    phone_number: str = None
    profile_img: str = None
    sns_type: str = None

    class Config:
        orm_mode = True"""
