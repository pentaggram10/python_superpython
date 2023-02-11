'''
-열거형 변수를 나타내는 자료구조 중 하나
<문법>
c=[] #빈 리스트
d=[1,2,3,4] #숫자들을 리스트로 나타냄
e=["사과","바나나","귤"]
f=[100,"체리",200,"블루베리"]

<특징1>
추가할 떄 append 메소드를 사용
맨 오른쪽에만 추가됨

<특징2>
제거할 떄 pop메소드 사용
맨 오른쪽 것만 제거

<특징3>
전체삭제할때 clear메소드 사용
빈 리스트로 바뀜

<특징4>
정렬(오름차순)할 떄 sort 메소드 사용
오름차순[1,2,3,4]
내림차순[4,3,2,1]

<특징5>
역순정렬 할 떄 reverse메소드 사용
'''

# c=[]
# d=[1,2,3,4]
# e=["사과", "바나나" ,"귤"]
# f=[100,"체리",200, "블루베리"]
# print(c)
# print(d)
# print(e)
# print(f)
# g=[]
# g.append(1)
# print(g)
# g.append("사과")
# print(g)
# g.append(2)
# g.pop()
# print(g)
# h=[1,"사과",2,"블루베리"]
# h.clear()
# print(h)
# i=[2,4,1,3]
# i.sort()
# print(i)
# j=["blueberry","orange","apple"]
# j.sort()
# print(j)
# k=[2,4,1,3]
# k.reverse()
# print(k)


# fruits=["blueberry","cherry","apple","watermelon"]
# fruits.sort()
# fruits.reverse()
# print(fruits)

# h=[]
# for i in range(1,21):
#     if i%3==0:
#         h.append(i)
# h.sort()
# h.reverse()
# print(h)


def 구구단(a):
    구굳=[]
    for i in range(a,a*9+1):
        if i%a==0:
            구굳.append(i)
            구굳.sort()
            구굳.reverse()
    print(구굳)
구구단(5)

