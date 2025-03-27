#서버 실행
import sys
import json

def main():
    # 입력 데이터 수신
    input_data = sys.argv[1]
    data = json.loads(input_data)

    # 수신 데이터 출력
    #print("Received data:", data)
    #print("Data received successfully")

    # 더미 데이터 생성
    response_data = {
        "answer": ["테스트 텍스트 전송"],
        "recommend": ["자료구조", "머신러닝", "알고리즘"]
    }
    sys.stdout.reconfigure(encoding='utf-8')
    # 더미 데이터 반환
    #sys.stdout.buffer.write(json.dumps(response_data, ensure_ascii=False).encode('utf-8'))

if __name__ == "__main__":
    main()


# Book 객체 리스트 생성



#todo

#db에 간단한 내용 추가하기. 일련번호

# 어떤 책이 있다.
# 사용자의 input 필요하당 + 어떤 책이 꽂혀있는 지도 파이썬상으론 받고 있다가,
# 사용자의 input 들어올 때마다 업데이트 해야한다. (그때 요청하기)
# DB가 어떻게 생겼는지 알아야함. 정제해줘잉

# input을 어떻게 받아야하나?
# 필요한 input
# 책의 실시간 위치(1 or 0)
# 사용자가 원하는 기능(1, 2, 3 ~ )
# 사용자의 자연어 입력

# 내 출력
# gpt의 출력(위치 정보도 같이 보내줘) 

# 책 DB는 처음부터 갖고 있어야한다.



# 16(일) 까지 1차 prototype deadline
# 24(월) 정기회의 버그 픽스
# 28(금) 정기회의 보고서 고치기



#추가 질문 구현하기.
#어떤 책 꺼낼지도
#책이 꽂혀있는지 확인하는 기능도 추가.
#책 검색기능?