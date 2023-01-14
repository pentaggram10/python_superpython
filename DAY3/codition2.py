'''
조건문2(while)
반복할 떄 사용
<문법>
while 조건:
    실행할 코드 작성
1)조건이 참이면 코드가 실행
2)조건이 거짓이면 while이 종료
True
False
이렇게 쓰자
'''

# a=0
# while a<3:
#     print("안녕")
#     a+=1

# a=1
# while a<11:
#     print(a)
#     a+=1

# a=2
# while a<11:
#     print(a)
#     a+=2

# a=1
# sum=0
# while a<21:
#     if a%4!=0:
#         sum+=a        
#     a+=1
# print(sum)

# a=50
# while a<101:
#     if a%2==0:
#         if a%3==0:
#            print(a)
#     a+=1
            
a=1
sum=0
mul=1
while a<11:
    if a%3==0:
        mul*=a
    if a%2==0:
        sum+=a
    a+=1
print(mul-sum)



 



