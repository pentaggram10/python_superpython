'''
생성자(constructor)
:객체를 생성할 떄 자동으로 호출되는 method
<문법>
class 클래스이름:
    def __init__(self):

'''
# class math:
#     원주율=3.141592
#     def 더하기(self,a,b):
#         결과=a+b
#         return 결과
# 초등수학=math()
# print(초등수학.원주율)
# print(초등수학.더하기(2,3))

# class 수학:
#     def __init__(self,반지름):
#         self.원주율=3.141592
#         self.반지름=반지름
#     def 원넓이(self):
#         결과=self.원주율*self.반지름**2
#         return 결과
# 고등수학=수학(2)
# print(고등수학.원넓이())

# class 개:
#     def __init__(self,이름,털색상):
#         self.이름=이름
#         self.털색상=털색상  
#     def 소개하기(self):
#         print(f"강아지 이름은 {self.이름}이고, 털은 {self.털색상}입니다")
# 멍=개("보리","노란색")
# 멍.소개하기()
# 삼멍=개("춘식이","무지개색")
# 삼멍.소개하기()

# class bank:
#     def __init__(self,accoundHolder,balance):
#         self.accountHolder=accoundHolder
#         self.balance=balance
#     def deposit(self,amount):
#         self.balance=self.balance+amount
#         print(f"{self.accountHolder}'s left amount is {self.balance}")
#     def withdrawal(self,amount): 
#         self.balance=self.balance-amount
#         print(f"{self.accountHolder}'s lef amount is {self.balance}")
     
# sinhanBank=bank("son",10000)
# sinhanBank.deposit(1000)
# sinhanBank.withdrawal(5000)
# ourBank=bank("sheep",10000)
# ourBank.deposit(50)
# ourBank.withdrawal(40)

class 연산:
    def __init__(self,첫번째수,두번째수):
        self.첫번째수=첫번째수
        self.두번째수=두번째수
    def 더하기(self):
        결과=self.첫번째수+self.두번째수
        print(f"두 수의 합은 {결과}")
    def 빼기(self):
        결과=self.첫번째수-self.두번째수
        print(f"두 수의 합은 {결과}")
    def 곱하기(self):
        결과=self.첫번째수*self.두번째수
        print(f"두 수의 곱은 {결과}")
    def 나누기(self):
        결과=self.첫번째수/self.두번째수
        print(f"두 수의 몫은 {결과}")    
첫번째수=input("첫번째수는:")
두번째수=input("두번째수는:")
사칙연산=연산(int(첫번째수),int(두번째수))
    
