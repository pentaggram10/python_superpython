import matplotlib.pyplot as plt
x=[]
y=[]
y2=[]
x2=[]
y3=[]
for i in range(-10,11):
        x.append(i)
        y.append(-i**2)
        y2.append(i**2)
subject=["korean","math","science"]
score=[60,90,70]
for i in range(-10,11):
        x2.append(i)
        y3.append(i**3)
bar_color1=["yellow","gold","darkgreen"]
bar_color2=["red","blue","green"]
figure,axes=plt.subplots(2,2)
axes[0,0].plot(x,y,'ro',x,y2,'go')
axes[0,1].bar(subject,score,color=bar_color1)
axes[1,0].barh(subject,score,color=bar_color2)
axes[1,1].plot(x2,y3,'k')
plt.show()
# x=[]
# y=[]
# y2=[]
# y3=[]
# y4=[]
# for i in range(-5,6):
#     x.append(i)
#     y.append(5)
#     y2.append(-5)
#     y3.append(5*i+10)
#     y4.append(-5*i+10)
# plt.figure()
# plt.plot(x,y,x,y2,x,y3,x,y4)