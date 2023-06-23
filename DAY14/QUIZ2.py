v=[]
sum=0
n=input("입력하세요")
int(n)
for i in n:
    for i in range(0,9):
        if n%i==0:
            sum+=n
            v.append(sum)
print(v)