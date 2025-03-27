from callGPT import ask_gpt


# gpt 자연어 output #LN
# 책 이름 #bok_name

def recommend(keyword: str, cnt, current_book):
    """
    상황에 맞는 책을 추천하는 기능
    """
    if cnt == 0:
        question = f"{keyword}라는 상황에 맞춰, {current_book} 중에서 추천해줘."
    else:
        question = keyword

    answer = ask_gpt(question, current_book)
    #print(answer)
    return answer
    
def recommendWithKeyword(keyword: str, cnt, current_book):
    """
    학습에 맞는 책을 추천하는 기능
    """
    if cnt == 0:
        question = f"{keyword}을 학습하고 싶어해. 가지고 있는 책 중에서 추천을 해줘."
    else:
        question = keyword
    return ask_gpt(question, current_book)

def search(keyword: str, cnt, current_book):
    """
    특정 키워드에 대한 공부법을 검색하는 함수
    """
    if cnt == 0:
        question = f"{keyword}를 키워드로, 가지고 있는 책 중에서 추천을 해줘."
    else:
        question = keyword
    
    return ask_gpt(question, current_book)