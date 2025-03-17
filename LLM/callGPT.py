import openai
from book import Book
openai.api_key = 'your_api'
""""""
book_descriptions = [
    {   "title": "해리 포터와 마법사의 돌",
        "author": "J.K. 롤링",
        "publisher": "문학수첩",
        "publication_year": 1997,
        "genre": "판타지",
        "summary": "해리 포터가 호그와트 마법학교에서 첫 해를 보내며 친구들과 함께 다양한 모험을 겪는 이야기.",
        "contents": ["1. 살아남은 아이", "2. 유리창 뒤의 사라진 유리", "3. 다이애건 앨리", "..."],
        "serial_number": "001",
        "current_location": "L1",
        "checkout_time": "1"
    },
    {   "title": "반지의 제왕",
        "author": "J.R.R. 톨킨",
        "publisher": "황금가지",
        "publication_year": 1954,
        "genre": "판타지",
        "summary": "프로도와 그의 친구들이 절대 반지를 파괴하기 위해 모험을 떠나는 이야기.",
        "contents": ["1. 반지의 동지", "2. 두 개의 탑", "3. 왕의 귀환", "..."],
        "serial_number": "002",
        "current_location": "서고 B-2",
        "checkout_time": "2025-03-12 14:00"
    },
    {   "title": "1984",
        "author": "조지 오웰",
        "publisher": "민음사",
        "publication_year": 1949,
        "genre": "디스토피아",
        "summary": "전체주의 사회에서 개인의 자유와 진실을 찾기 위한 윈스턴 스미스의 이야기.",
        "contents": ["1. 제1부", "2. 제2부", "3. 제3부", "..."],
        "serial_number": "003",
        "current_location": "서고 C-3",
        "checkout_time": "2025-03-12 14:00"
    },
    {   "title": "위대한 개츠비",
        "author": "F. 스콧 피츠제럴드",
        "publisher": "문학동네",
        "publication_year": 1925,
        "genre": "고전",
        "summary": "제이 개츠비와 그의 사랑, 그리고 미국의 꿈에 대한 이야기.",
        "contents": ["1. 닉의 이야기", "2. 개츠비의 파티", "3. 개츠비와 데이지", "..."],
        "serial_number": "004",
        "current_location": "서고 D-4",
        "checkout_time": "2025-03-12 14:00"
    },
    {   "title": "호밀밭의 파수꾼",
        "author": "J.D. 샐린저",
        "publisher": "민음사",
        "publication_year": 1951,
        "genre": "고전",
        "summary": "홀든 콜필드의 성장과 방황을 그린 이야기.",
        "contents": ["1. 홀든의 이야기", "2. 뉴욕에서의 방황", "3. 피비와의 만남", "..."],
        "serial_number": "005",
        "current_location": "서고 E-5",
        "checkout_time": "2025-03-12 14:00"
    }  
]
""""""
"""
book_descriptions = [
    {   
        "title": "해리 포터와 마법사의 돌",
    },
    {   
        "title": "반지의 제왕",
    },
    {   
        "title": "1984",
    },
    {   
        "title": "위대한 개츠비",
    },
    {   
        "title": "호밀밭의 파수꾼",
    }  
]
"""
books = [Book(**description) for description in book_descriptions]

def ask_gpt(question: str) -> str:
    """
    GPT-4에게 질문을 보내고 응답을 받는 함수.
    """
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You are a helpful assistant. You have this books: {books}."},
                {"role": "user", "content": f"{question}"},
            ],
            temperature = 0.1,
            max_tokens = 300,  # 최대 토큰 수 제한
        )
        answer = response.choices[-1].message.content
        return answer
    except Exception as e:
        return f"Error: {str(e)}"