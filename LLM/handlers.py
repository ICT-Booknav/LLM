from callGPT import ask_gpt

def recommend(keyword: str, cnt):
    """
    상황에 맞는 책을 추천하는 기능
    """
    if cnt == 0:
        question = f"{keyword}라는 상황에 맞춰, 가지고 있는 책의 위치를 같이 추천해줘."                   
    else:
        question = keyword
        
    return ask_gpt(question)
    
def recommendWithKeyword(keyword: str, cnt):
    """
    학습에 맞는 책을 추천하는 기능
    """
    if cnt == 0:
        question = f"{keyword}을 학습하고 싶어해. 가지고 있는 책 중에서 추천을 해줘."  
    else:
         question = keyword
    return ask_gpt(question)

def search(keyword: str, cnt):
    """
    특정 키워드에 대한 공부법을 검색하는 함수
    """
    if cnt == 0:
        question = f"{keyword}를 키워드로, 가지고 있는 책 중에서 추천을 해줘." 
    else:
        question = keyword
    return ask_gpt(question)