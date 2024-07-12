from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
from supabase import create_client, Client
from dotenv import load_dotenv
import os

app = FastAPI()

# リクエストボディのデータ構造を定義
class Item(BaseModel):
    name: str

load_dotenv()

supabase_url: str = os.getenv("SUPABASE_URL")
supabase_key: str = os.getenv("SUPABASE_KEY")
print(supabase_url,supabase_key)

# 環境変数が正しく読み込まれているか確認
if not supabase_url or not supabase_key:
    raise Exception("Supabase URL and Key must be set in environment variables")

supabase: Client = create_client(supabase_url, supabase_key)

# ルーティングの設定
@app.post("/items/")
async def create_item(item: Item):
    return {"name": item.name}

#ここを変える
@app.post("/test")
async def find_all_data():
    data = supabase.table("test").insert({"text": "ほげほげ"}).execute()
    return data.data


# サーバー起動
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)