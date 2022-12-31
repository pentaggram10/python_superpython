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
# apple=30
# orange=20
# if apple>orange:
#     print("사과가 큼")
# else:
#     print("오렌지가 큼")


# for i in range(3):
#     print("안녕")

# i=1
# for i in range(1,11):
#     print(i)

# i=1
# for i in range(2,11,2):
#     print(i)

# i=1
# for i in range(1,11):
#     if i%2==1:
#         print(i)

# i=1
# for i in range(1,11):
#     if i%2==0:
#         print(i)

# i=1
# sum=0
# for i in range(20,41):
#     if i%3!=0:
#         sum+=i

# print(sum)

# i=1
# for i in range(50,101):
#     if i%3==0:
#         if i%4==0:
#             print(i)

# sum=0
# sum2=0
# for i in range(1,101):
#     if i%2==0:
#         sum+=i
#     if i%2!=0:
#         sum2+=i

# print(sum-sum2)

mul=1
for i in range(10,31):
    if i%9==0:
        mul*=i

print(mul)