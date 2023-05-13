'''
클래스(class)
-객채(object)를 생성하기 위한 설계도
-생성된 객체는 인스턴스(instance)라고 함
-class 내 멤버변수는 프로퍼티 라고 함(property)
-class 내 멤버함수는 메소드라고 함(method)
<문법>
class 클래스이름:
    property
    method

*메소드 작성시 입력변수로 self를 반드시 적어줘야함
'''
# class 수학:
#     원주율=3.14 
#     자연로그e=2.718
#     def 더하기(self,a,b):
#         합=a+b
#         return 합
# 초등수학=수학()
# print(초등수학.원주율)
# 중등수학=수학()
# print(중등수학.원주율)
# 고등수학=수학()
# print(f"{고등수학.원주율},{고등수학.자연로그e}")
# 유치원수학=수학()
# print(유치원수학.더하기(1,2))

# def 더하기(a,b):
#     합=a+b
#     return 합
# print(더하기(1,2))
class 수학:
    def 부피(self,a,b):
        결=3.14*a*a*b
        return 결
    def 겉넓이(self,a,b):
        결과=2*3.14*a*b+3.14*a*a+3.14*a*a
        return 결과
반지름=input("반지름을 입력하세요:")
높이=input("높이 입력:")
중등수학=수학()
print(f"반지름이 {반지름}이고, 높이가{높이}일 떄, 원기둥 겉넓이는{중등수학.겉넓이(int(반지름),int(높이))}이고,원기둥 부피는{중등수학.부피(int(반지름),int(높이))}입니다")

