import matplotlib.pyplot as plt
import numpy as np
plt.figure()
x=[]
y=[]
x2=[]
y2=[]
x3=[]
y3=[]
x4=[]
y4=[]
for i in range(-10,11):
    x.append(i)
    y.append(-i)
    x2.append(i)
    y2.append(i)
    x3.append(i)
    y3.append(i**2)
    x4.append(i)
    y4.append(-i**2)
plt.plot(x,y,'ro',x2,y2,'go',x3,y3,'bo',x4,y4,'o')
plt.show()


# x=[]
# y=[]
# for i in range(-10,11):
#     x.append(i)
#     y.append(-2*i+1)
#     plt.plot(x,y)

# x=[]
# y=[]
# for i in range(-20,21):
#     x.append(i)
#     y.append(-i**2)
# plt.plot(x,y)

# x=[]
# y=[]
# for i in range(-10,11):
#     x.append(i)
#     y.append(-2*i**3)
# plt.plot(x,y)

# x=[]
# y=[]
# x2=[]
# y2=[]
# for i in range(-10,11):
#     x.append(i)
#     y.append(2**i)
#     x2.append(i)
#     y2.append(1/2**i)
# plt.plot(x,y,x2,y2)
# x=[]
# y=[]
# for i in range(-60,70):
#     x.append(i/10)
#     y.append(np.tan(i/10))
# plt.plot(x,y)