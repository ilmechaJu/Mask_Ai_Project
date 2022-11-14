from dataclasses import asdict
from typing import Optional

import uvicorn
from fastapi import FastAPI, UploadFile, File
import shutil

# from app.database.conn import db
# from app.common.config import conf
from app.routes import index


def create_app():

    app = FastAPI()
    # c = conf()
    # conf_dict = asdict(c)
    # db.init_app(app, **conf_dict)
    # 데이터 베이스 이니셜라이즈

    # 레디스 이니셜라이즈

    # 미들웨어 정의

    # 라우터 정의
    app.include_router(index.router)
    # app.include_router(auth.router, tags=["Authentication"], prefix="/auth")
    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)


@app.post("/img")
async def root(file: UploadFile = File(...)):
    with open(f"{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"file_name": file.filename}
