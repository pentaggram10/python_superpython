'''
딕셔너리(dictionary)
python에서 사용하는 자료구조
key와 value의 쌍으로 이루어짐
중괄호와 :를 이용해 작성
ex){"손흥민":축구,"류현진":"야구"}
"손흥민","류현진=key
"축구","야구"=value
indexing 가능-> key 이용
            -> get method 이용해도 됨
indexing을 이용한 수정 또는 update method를 이용해 value를 바꿀 수 있음
update method를 이용해 value쌍을 추가할 수 있음
'key in dictionary' 질문에 True/False로 확인 가능 
'''

# height={"용규":177,"자민":200,"재민":125,"준영":101}
# print('용규' in height)
# print('손흥민' in height)
# print(height)
# 리스트=[177,200,125,101]
# 리스트[1]=150
# print(리스트)

fruits={'orange':50,'banana':30,'apple':40}
fruit=input("This is fruit store. what do you want?")
if fruit in fruits:
    print(f"we have {fruit}, {fruits[fruit]} left")    
else :
    print(f"sorry, we don't have {fruit}")
   