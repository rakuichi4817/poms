"""バックエンドアプリの基本設定内容"""
from pydantic import BaseSettings


class Settings(BaseSettings):
    """APIサーバの設定項目"""

    TITLE = "poms API"
    DESCRIPTION = "pomsのバックエンドAPI"
    VERSION = "0.1.0"

    ORIGINS = ["http://localhost", "http://localhost:8501"]

    API_PREFIX = "/api/v1"


class MainDevSettings(Settings):
    """本番、開発環境の設定内容

    Notes
    -----
    インスタンス設定などを追加
    """

    pass
