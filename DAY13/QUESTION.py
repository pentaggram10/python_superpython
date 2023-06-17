a=[0,0,0,0,0,0,0,0,0,0]
for i in range(0,1000):
    for n in str(i):
        a[int(n)]+=1
print(a)
