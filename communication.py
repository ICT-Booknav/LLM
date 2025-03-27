import sys
import json
import asyncio
from pydantic import BaseModel
from handlers import recommend, search, recommendWithKeyword
from typing import List

cnt = 0
prev_type = None

bookdata = [
    ('000000000000000001', '자료구조'),
    ('000000000000000002', '해리포터와_마법사의_돌'),
    ('000000000000000003', '해저2만리'),
    ('000000000000000004', '자바의_정석_2'),
    ('000000000000000005', '파이썬_완벽_가이드'),
    ('000000000000000006', '클린코드'),
    ('000000000000000007', '인간_본성의_법칙'),
    ('000000000000000008', '성공하는_사람들의_7가지_습관'),
    ('000000000000000009', '돈의_심리학'),
    ('000000000000000010', '생각의_기술'),
    ('000000000000000011', '종의_기원')
    ]
bookdata = {item[0]: item[1] for item in bookdata}
current_book = []


class RequestData(BaseModel):
    type: str = 1  # 1: 추천li, 2: 검색
    question: str = None # 검색 키워드 (선택적)
    bookshelfData: List[str]

#출력 포맷 바꾸기
def process_booknames(response: str, bookname: str) -> dict:
    """
    Splits the bookname string into a list and returns a dictionary with the response and processed booknames.
    """

    result = bookname.split(",")
    
    # Create a dictionary where each bookname is labeled
    bookname_dict = {f"bookname{i+1}": name.strip() for i, name in enumerate(result)}
    
    # Return the final dictionary with both the response and processed booknames
    return {
        "answer": response,
        "booknames": bookname_dict
    }



async def handle_gpt_request(data: RequestData):
    #print(f"555", {data.keyword})
    current_book.clear()
    #print(data.bookshelfData)
    for book_id in data.bookshelfData:
        current_book.append(bookdata[book_id.strip()])
    #print(current_book)
    

    if data.type !=None:
        cnt = 0
        prev_type = data.type
    else:
        data.type = prev_type

    if data.type == "1":
        response, bookname = recommend(data.question, cnt, current_book)

    elif data.type == "2":
        response, bookname = recommendWithKeyword(data.question, cnt, current_book)

    elif data.type == "3":
        response, bookname = search(data.question, cnt, current_book)
    else:
        response = "잘못된 요청입니다. type을 확인하세요."
        cnt -= 1
    cnt += 1


    #print(response)
    response = response.encode('utf-8')
    answer = process_booknames(response.decode('utf-8'), bookname)
    #print("123", response)
    #sys.stdout.buffer.write(json.dumps(response, ensure_ascii=False).encode('utf-8'))
    return answer

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    input_data = sys.argv[1]
    #print(f"Raw input_data: {input_data}")  # 디버깅용 출력
    data_dict = json.loads(input_data)
    #print(f"Parsed data_dict: {data_dict}")  # 디버깅용 출력
    data = RequestData(**data_dict)
    #print(f"RequestData object: {data}")  # 디버깅용 출력
    response = asyncio.run(handle_gpt_request(data))
    response_json = json.dumps(response, ensure_ascii=False).encode('utf-8')
    sys.stdout.buffer.write(response_json)
    #sys.stdout.buffer.flush()
    #sys.stdout.buffer.write(json.dumps(response, ensure_ascii=False).encode('utf-8'))
    


if __name__ == "__main__":
    main()