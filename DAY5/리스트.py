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

<특징6>
값으로 자리를 찾는 메소드
중복된 값이 있을 경우 맨 왼쪽 값만 출력
리스트에 없는 값은 에러남

<특징7>
indexing(문법)
자리로 값을 출력하는 문법
[]와 숫자 사용
left to right 방식에서는 0부터 시작
right to left 방식에서는 -1부터 시작

<특징8>
원하는 자리에 값을 추가할 떄 insert 메소드 사용
c=["cherry","apple","banana"]
c.insert(1,orange)
print(c)

<특징9>
원하는 값을 제거할 떄 remove 메소드 사용

<특징10>
값들의 개수를 셀 때 count 메소드 사용

<특징11>
리스트와 리스트를 결합할 때
extend 메소드 사용

<특징12>
리스트와 리스트를 결합할 떄 +연산자 사용가능

<특징13>
리스트의 길이를 알고싶을 때
len 함수 사용

<특징14>
fruits=["cherry","orange","apple"]
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

# a=[100,200,300,400]
# a.append(100)
# print(a.index(100))

# def 구구단(a):
#     구굳=[]
#     for i in range(a,a*9+1):
#         if i%a==0:
#             구굳.append(i)
#             구굳.sort()
#             구굳.reverse()
#     print(구굳)
# 구구단(5)

# b=[100,200,300,400]
# print(b[0]+b[2])
# print(b[-1]-b[1])
# print(b[-2]%b[1])

# c=["cherry","apple","banana"]
# c.insert(1,"orange")
# c.insert(3,"watermelon")
# c.remove("cherry")
# print(c)

# d=[1,2,3,1,4]
# print(d.count(5))

# e=[1,2,3]
# f=[4,5]
# e.extend(f)
# print(e)
# f.extend(e)
# print(f)

# g=[1,2,3]
# h=[4,5]
# print(g+h)
# print(h+g)

# i=[10,20,30]
# print(len(i))
# i.append(40)
# print(len(i))
# i.clear()
# print(len(i))

# fruits=["cherry","orange","apple"]
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])


# fruits=["cherry","orange","apple"]
# fruits.append("watermelon")
# fruits.insert(2,"banana") 
# fruits.sort()
# fruits.reverse()      
# for i in range(len(fruits)):
#     print(fruits[i])

numbers=[]
for i in range(1,20):
    if i%3==0:
        numbers.append(i)
print

numbers.sort()
numbers.reverse()
for i in range(len(numbers)):
    print(numbers[i])


