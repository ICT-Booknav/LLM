from fastapi import FastAPI
from pydantic import BaseModel
from handlers import recommend, search, recommendWithKeyword

app = FastAPI()
app.state.cnt = 0
app.state.prev_type = None
class RequestData(BaseModel):
    type: int = None # 1: 추천, 2: 검색
    keyword: str = None # 검색 키워드 (선택적)




@app.post("/gpt")
async def handle_gpt_request(data: RequestData):
    #처음 질문의 경우 type이 존재할거라는 가정
    
    #data.type이 있으면, 저장한다 + cnt값을 초기화한다.
    #새로운 맥락이라는 판단
    if data.type != None:
        app.state.cnt = 0
        app.state.prev_type = data.type
    #값이 정해지지 않았다면, 이전 질문과 같은 곳으로 간다.
    else:
        data.type = app.state.prev_type
    """
    type 값에 따라 다른 기능을 수행
    """
    
    if data.type == 1:
        response = recommend(data.keyword, app.state.cnt)


    elif data.type == 2:
        response = recommendWithKeyword(data.keyword, app.state.cnt)

    elif data.type == 3:
        response = search(data.keyword, app.state.cnt)
    else:
        response = "잘못된 요청입니다. type을 확인하세요."
        app.state.cnt -= 1
    app.state.cnt += 1        
    return {"answer": response}
