'''
함수
-반복적인 작업을 할 때 유용하게 사용 가능
-만드는 과정과 사용하는 과정으로 분류할 수 있음
<문법1>
def 함수이름():
->함수내용 작성

함수이름()

<문법2>
def 함수이름(입력):
->함수내용 작성 (입력을 이용할 수 있음)
*숫자,문자 대신 변수로 표기
*입력이 여러개라면 쉼표로 구분해서 입력
def 함수이름(입력1,입력2,....)
->

<문법3>
def 함수이름(입력):
->함수내용 작성
  return 결과
  *입력과 결과 모두 변수로 표기
'''
# def 토요일():
#     print("와 토요일이다")

# 토요일()
# 토요일()

# def 일요일(숫자):
#     for i in range(숫자):
#         print("일요일은 뭐하지")

# 일요일(5) 

# def 거듭제곱(밑,지수):
#     결과=밑**지수
#     return 결과
# value=거듭제곱(2,3)
# print(value)
# print(거듭제곱(3,3))

# def 합차곱나(앞,뒤):
#     결과=앞+뒤
#     결과1=앞-뒤
#     결과2=앞*뒤
#     결과3=앞/뒤
#     return 결과,결과1,결과2,결과3
# print(합차곱나(4,2))
# print(합차곱나(10,2))

# def 구구단(수):
#     for i in range(1,10):
#         print(수*i)
# 구구단(3)
# 구구단(7)

def 짝수(수):
    for i in range(2,수*2+1):
        if i%2==0:
            print(i)
짝수(4)
짝수(7)
짝수(3)
       