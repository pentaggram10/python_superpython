# a=[0,0,0,0,0,0,0,0,0,0]
# for i in range(1,1001):
#     charI=str(i)
#     for n in charI:
#         idx=int(n)
#         a[idx]+=1
# print(a)

# arr=[-2,3,2,-5,7]
# neg=[]
# pos=[]
# for i in arr:
#     if i<0:
#         neg.append(i)
#     else:
#         pos.append(i)
# print(neg+pos)

sum=0
for i in range(1,1001):
    if i%3==0:
        sum+=i
    elif i%5==0:
        sum+=i
print(sum)