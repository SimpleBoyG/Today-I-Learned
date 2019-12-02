#=============== class(미완)==================================
class Person:
    def greetion(self):
        print('Hello')

#=============== Ex_01_class ======================================
class fruits:
    def cup1(self):
        print('apple')
    def cup2(self):
        print('pear')
    def cup3(self):
        print('pineapple')
    def cup4(self):
        print('banana')

juice = fruits()
juice.cup1() # instance(인스턴스)

#============== method ==========================================
a = list(range(1,6))
print(a)
a.append(6) #메~~소드
print(a)

#============= Exemple 1 ===========================================
class Person:
    def __init__(self, name, age, address):
        self.hello = '안녕하세요'
        self.name = name
        self.age = age
        self.address = address
    def greeting(self):
        print('{0} 저는 {1}입니다.'.format(self.hello, self.name))

gildong = Person('홍길동', 20, '서울시 서초구 반포동')
gildong.greeting()


print('이름:',gildong.name)
print('나이:',gildong.age)
print('주소:',gildong.address)

#============= Exemple 2 ===========================================
class zoo:
    def tiger(self, name, age, location):
        self.hello = '어흥 난 호랑이다'
        self.name = name
        self.age = age
        self.location
    def greeting(self): 
        print('{0} 나 무섭지? 난 {2}')

class Person1:
    def __init__(self, *args):
    
        self.name = args[0]
        self.age = args[1]
        self.address = args[2]
    

jjs = Person('정준상',29,'서울시 금천구 가산동')
jej = Person('정은진',32,'창원시 진해구 자은동')

#정준상
print('이름 : ',jjs.name,'\n','나이 : ',jjs.age,'\n','주소 : ',jjs.address)
#정은진
print('이름 : ',jej.name)
print('나이 : ',jej.age)
print('주소 : ',jej.address)
print()

#================= 딕셔너리 ================================================
# class Person2:
#     def __init__(self, **kwargs):
#         self.name=kwargs['name']
#         self.age=kwargs['age']
#         self.address = kwargs['address']

# kate = Person2(name='케이트', age = 20, address = '서울 서초구 반포동')
# print(kate.name)


#===================== Exemple ============================================
# class Person3:
#     def greeting(self):
#         self.hello = '안녕하세요.'

# maria = Person3()
# maria.hello


# class Person4:
#     __slots__ = ['name', 'age']
#     def __init__(self,**kwargs):
#         self.name = kwargs['name']
#         self.age = kwargs['age']

# dragon = Person3(name = '드레곤', age = 3, address = '서울시')
# dragon.name

#============== 클래스 내부에서 변수 선언 ===================================
class Person5 :
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet

terry = Person5('테리', 20, '서울시 서초구', 10000)
terryname = terry.name
print(terryname)
print()


class Person6 :
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet
    def pay(self, amount):
        self.__wallet -= amount

        if self.__wallet > 0:
            print('이제 {0}원 남았습니다.'.format(self.__wallet))
        else:
            print('이제 {0}원 남았습니다.'.format(self.__wallet)) 
            print('잔고 부족입니다.')

terry = Person6('테리', 20, '서울시 서초구', 10000)
terrypay = terry.pay(5000)
terrypay
terrypay = terry.pay(3000)
terrypay
terrypay = terry.pay(3000)
terrypay
