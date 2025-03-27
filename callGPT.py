import openai
import os

api_key = os.getenv("OPENAI_API_KEY")

openai.api_key = api_key

def ask_gpt(question: str, current_book) -> str:
    """
    GPT-4에게 질문을 보내고 응답을 받는 함수.
    """
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You are a helpful assistant. Give me answer just natural language. You have this books:.{current_book}"},
                {"role": "user", "content": f"{question}"},
            ],
            temperature = 0.1,
            max_tokens = 300,  # 최대 토큰 수 제한
        )
        answer = response.choices[-1].message.content
        answer.encode('utf-8')

        response2 = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                #{"role": "system", "content": f"You are a helpful assistant. You have this books: {books}."},
                {"role": "user", "content": f"{answer}에서 책 이름만 그대로 출력해줘. 만약 두 개 이상이면 ,로 구분해줘"},
            ],

            temperature = 0.0,
            max_tokens = 300,  # 최대 토큰 수 제한
        )
        answer2 = response2.choices[0].message.content
        answer2.encode('utf-8') 
        #print(answer)
        #print(answer2)

        return answer, answer2
    except Exception as e:
        return f"Error: {str(e)}"