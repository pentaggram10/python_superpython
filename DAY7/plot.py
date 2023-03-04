'''
모듈(module)설치
-pip install 모듈이름

모듈 가져오기
-import 모듈이름

모듈 사용하기
모듈이름.변수
모듈이름.함수
'''
import matplotlib.pyplot as fu
# fu.figure()  
# fu.plot([50,40,60],[150,120,200],'go')
# fu.ylabel("height")
# fu.xlabel('weight')
# fu.show()
xvalues=[]
yvalues1=[]
yvalues2=[]
yvalues3=[]
for i in range(-10,10):
    xvalues.append(i)
    yvalues1.append(i)
    yvalues2.append(i*i)
    yvalues3.append(i**3)
fu.figure()
fu.plot(xvalues,yvalues1,'r',xvalues,yvalues2,'g',xvalues,yvalues3,'b')
fu.ylabel("y")
fu.xlabel("x")
fu.show()