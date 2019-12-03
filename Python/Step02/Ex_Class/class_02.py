#============각자의 가방에 넣기(이거 어려운데?) ============
class Person:
    
    def __init__(self):
        self.bag=[] # 값 초기화
        
    def put_bag(self, stuff): #가방에 넣는다
        self.bag.append(stuff)
    

jjs = Person()
jej = Person()

jjs.put_bag('money')
print(jjs.bag)
jej.put_bag('water')
print(jej.bag)

#============= 비공개 클래스 속성(Private attribute) 사용하기 ============================
#비공개 속성은 앞에 __(언더바두개)를 함으로써 비공개라 선언해준다.
# class Knight:
#     __item_limit = 10
#     def print_item_limit(self):
#         print(Knight.__item_limit) # 내부에서만 사용

#     x = Knight()
#     x.print_item_limit()

#============= 정적 매서드(class에 바로 호출하는) 방식 ====================================
class calc : 
    @staticmethod
    def add(a,b):
        print(a+b)
    
    @staticmethod
    def mul(a,b):
        print(a*b)

calc.add(10,20)
calc.mul(10,20)
#인스턴스의 상태를 변화시키지 않는 상태를 만들 떄 사용하며, @는 데코레이터라 함.
#self는 사용하지 않는다.

#============================ 클래스 매소드 사용하기 =============================================
class Person:
    count = 0
    def __init__(self):
        Person.count += 1
    @classmethod
    def print_count(cls):
        print('{0}명 생성되었습니다.'.format(cls.count))
    
jjs = Person()
jej = Person()
huh = Person()
Person.print_count()
# cls는 클래스 메소드의 전용 매개변수이다.
# class 클래스 이름:
#     @classmethod
#     def 매서드(cls, 매개변수 1, 매개변수 2):
#         ~코드
# *주의 : classmethod 사용, 클래스 매개변수는 첫번째 매개변수에 cls지정(class에서 따옴.)

 
