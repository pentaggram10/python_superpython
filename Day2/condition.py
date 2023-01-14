'''
조건문
1.IF,ELSE
if 조건:
    참일떄 작성
else:
    거짓일때 작성

2.FOR
for 변수 in range(숫자):
    작성
for 변수 in range(시작,끝):
    작성
for 변수 in range(시작,끝,증감):
    작성
'''
# 만약 사과가 크다면 사과가 크다고 출력하고 아니면 오렌지가 크다고 출력
apple=30
orange=20
if apple>orange:
    print("사과가 큼")
else:
    print("오렌지가 큼")

#안녕 3번 프린트
for i in range(3):
    print("안녕")

#1부터 10까지 출력
i=1
for i in range(1,11):
    print(i)

#1부터 10중 2의 배수만 출력
i=1
for i in range(2,11,2):
    print(i)

#1부터 10중 소수만 출력
i=1
for i in range(1,11):
    if i%2==1:
        print(i)

#1부터 10중 짝수 출력
i=1
for i in range(1,11):
    if i%2==0:
        print(i)

#20부터 40중 3의 배수가 아닌 것들의 합
i=1
sum=0
for i in range(20,41):
    if i%3!=0:
        sum+=i
print(sum)

#50에서 100중 12의 배수 출력
i=1
for i in range(50,101):
    if i%3==0:
        if i%4==0:
            print(i)

#1부터 100중 2의 배수인 것의 합과 아닌 것들의 합의 차
sum=0
sum2=0
for i in range(1,101):
    if i%2==0:
        sum+=i
    if i%2!=0:
        sum2+=i
print(sum-sum2)

#10부터 30중 9의 배수들의 곱
mul=1
for i in range(10,31):
    if i%9==0:
        mul*=i
print(mul)