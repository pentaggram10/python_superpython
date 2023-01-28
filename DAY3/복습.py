"100~110중 홀수만 출력"
# i=100
# for i in range(100,111):
#     if i%2!=0:
#         print(i)
#     i+=1

# a=100
# while a<111:
#     if a%2!=0:
#         print(a)
#     a+=1
"100~200중 2와 3과 5의 공배수 출력"
# i=100
# for i in range(100,201):
#     if i%2==0:
#         if i%3==0:
#             if i%5==0:
#                 print(i)
# i+=1

# a=100
# while a<201:
#     if a%2==0:
#         if a%3==0:
#             if a%5==0:
#                 print(a)
#     a+=1 

"1~10중 3의 배수가 아닌 수들의 합"

i=0
sum=0
for i in range(11):
    if i%3!=0:
        sum+=i
        i+=1
print(sum)

a=0
sum=0
while a<11:
    if a%3!=0:
        sum+=a      
    a+=1 
print(sum)