"""エンドポイントの設定

routers内に作成したエンドポイントを指定
"""
from fastapi import APIRouter

from backend.v1.routers import samples


# 各種モジュールの設定
api_router = APIRouter()
api_router.include_router(samples.router, tags=["サンプル"], prefix="/sample")
