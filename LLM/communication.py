from fastapi import FastAPI
from pydantic import BaseModel
from handlers import recommend, search, recommendWithKeyword

app = FastAPI()

class RequestData(BaseModel):
    type: int  # 1: 추천, 2: 검색
    keyword: str = None # 검색 키워드 (선택적)

@app.post("/gpt")
async def handle_gpt_request(data: RequestData):
    """
    type 값에 따라 다른 기능을 수행
    """
    if data.type == 1:
        response = recommend()

    elif data.type == 2:
        response = recommendWithKeyword(data.keyword)

    elif data.type == 3:
        response = search(data.keyword)
    else:
        response = "잘못된 요청입니다. type을 확인하세요."
    
    return {"answer": response}
