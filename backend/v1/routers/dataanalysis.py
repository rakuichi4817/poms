import random
from datetime import datetime

import pandas as pd
from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from backend.schemas import dataanalysis as schema_dataanalysis

router = APIRouter()


@router.post("/generate-table")
async def generate_table(query: schema_dataanalysis.GenerateTableIn):
    """# csvファイルの生成

    リクエストされた項目条件をもとにcsvファイルを作成する
    """

    records = {}
    for column in query.columns:
        # 各項目毎に作成する
        if column.column_type == "int":
            # 整数の時
            records[column.column_name] = [
                random.randint(column.min_val, column.max_val) for i in range(query.record_cnt)
            ]
        elif column.column_type == "float":
            # 少数の時
            records[column.column_name] = [
                random.uniform(column.min_val, column.max_val) for i in range(query.record_cnt)
            ]

    df = pd.DataFrame(records)
    return StreamingResponse(
        iter([df.to_csv(index=False)]),
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename={datetime.now().strftime('%Y-%m-%d_%H:%M:%S')}.csv"},
    )
