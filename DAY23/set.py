# a=[1,2,3]
# print(a[1])
# b=[1,2,3]
# print(b[1])
# a.append(4)
# print(a)
# c={"야구":"류현진","축구":"손흥민"}
# print(c["야구"])
# a={1,2,3,4,5}
# b=set([4,5,6,7,8])
# c=a&b
# d=a.intersection(b)
# e=b.intersection(a)
# f=a|b
# g=b|a
# h=a.union(b)
# i=b.union(a)
# j=a-b
# k=b-a
# l=a.difference(b)
# m=b.difference(a)
# n={100,200,300}
# n.update([400,500,600])
# a.add(100)
# a.add(200)
# b.add(100)
# a.remove(5)
# b.remove(7)
# print(n)
# print(b&a)
# print(a|b)
# print(a)
# print(b)
# print(a&b)
# print(a)
# print(b)
# print(type(a),type(b))
# print(c)
# print(d)
# print(e)
# print(f,g)
# print(h,i)
# print(j)
# print(k)
# print(l,m)
# a=set("Hello python")
# b=set("welcome math")
# print(a&b)
# print(a|b)
# print(a-b)
# print(b-a)
a={1,2,3,4,6,12}
b={1,2,4,5,10,20}
print(max(a&b))
print(min(a-b)*min(b-a)*max(a&b))
