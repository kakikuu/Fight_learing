from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI()


# リクエストボディのデータ構造を定義
class Item(BaseModel):
    name: str


# ルーティングの設定
@app.post("/items/")
async def create_item(item: Item):
    return {"name": item.name}


# サーバー起動
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
