from fastapi import APIRouter, Depends, File
from starlette.responses import Response

from backend.schemas import samples
from backend.libs.images import face_mosaic


router = APIRouter()


@router.get("/plus", response_model=samples.AddOut)
async def add(query: samples.AddIn = Depends()):
    """足し算

    Parameters
    ----------
    a : int | float
        足される数\\
    b : int | float
        足す数
    """
    return {"result": query.a + query.b}


@router.post("/mosaic")
async def mosaic(file: bytes = File(..., description="モザイクをつける画像")):
    """顔にモザイクを追加する

    Parameters
    ----------
    file_byte : byts
        画像データ
    """
    mosaic_byte = face_mosaic(file)
    return Response(mosaic_byte, media_type="image/png")
