
class Person: #(Super class)
    def greeting(self):
        print("안녕하세요")

class Student(Person): #Person으로 상속을 받는다.(Sub class)
    def study(self):
        print('공부하기')
# 자식으로 설정하고 부모를 호출 할 경우
james = Student()
james.greeting() # 부모 호출 가능
james.study() #자식 호출 가능
print()

# 부모를 설정하고 자식을 호출 할 경우
bam = Person()
bam.greeting() # 부모 호출 가능
# bam.study() # 자식 호출 불가능
print()

#=================== Pass ===============================
# class Person1:
#     pass

# class Student1(Person1):
#     pass

# issueclass(Student1, Person1)

#====================포함(include)=========================
class Person:
    def greeting(self):
        print('Hello!')

class Personlist:
    def __init__(self):
        self.person_list = []
    def append_person(self, person):
        self.person_list.append(person)

a = Personlist()
a.append_person('sam')
# print(a.pe)

#============상속을 받았지만 호출을 할 수 없는 경우====================
class Person:
    def __init__(self):
        print('Person __init__')
        self.hel = '안녕하세요'

# class Student(Person):
#     def __init__(self): 
#         print('Studenf__init__')
#         self.school = '파이썬 강의장'

# james = Student()
# print(james.school)
#print(james.hel) # __init__에서 제한이 걸려 부모를 호출할 수 없다

#따라서 다음의 예를 사용하여 부모 클래스에 접근한다.

class Student(Person):
    def __init__(self):
        print('Studenf __init__')
        super().__init__() #super를 사용하여 부모클래스의 __init__함수에 접근
        self.school = '파이썬 강의장'

james = Student()
print(james.school)
print(james.hel)
print()

class Student1(Person):
    pass

b = Student1() #자식의 __init__이 설정이 안 된 경우 부모까지 거슬러 올라가 __init__을 출력한다.
print(b.__init__)

class Student2(Person):
    def __init__(self):
        print('Student__init__')
        super(Student2, self).__init__()
        self.school = '파이썬'

b = Student2()
print(b.school)
print(b.hel)
print()

#=================오버라이딩(Overriding)========================
class Person2:
    def greeting(self):
        print('안녕하세요')

class Student3(Person2):
    def greeting(self):
        print('여기는 Student class !!!')

c = Student3()
c.greeting()
print()

class Student4(Person2):
    def greeting(self):
        super().greeting()
    
d = Student4()
d.greeting()
print()

#===========================
class University:
    def manage_credit(self):
        print('학점관리')

class Graduate(Person2, University):
    def study(self):
        print('공부하기')

e = Graduate()
e.study()
e.greeting()
e.manage_credit()
print()

# +,-,*,/의 여러 부모에게서 상속받아 출력하기
class Add:
    def Add1(self,a,b):
        print(a+b)

class Minus:
    def Minus1(self,a,b):
        print(a-b)

class Mul:
    def Mul1(self,a,b):
        print(a*b)

class Div:
    def __init__(self):
        self.a = a
        self.b = b
    def Div1(self,a,b):
        print(int(a/b))

class answer(Add,Minus,Mul,Div):
    pass

person = answer()
person.Add1(10,5)
person.Add1(10,5)
person.Minus1(10,5)
person.Mul1(10,5)
person.Div1(10,5)

#==================== 별해(이우용) ===============================
class Plus():
    def Plus_input(self,a,b):
        return a+b

class Minus():
    def Minus_input(self,a,b):             
        return a-b

class Plus():
    def Plus_input(self,a,b):
        return a+b

class Minus():
    def Minus_input(self,a,b):
        return a-b

class Mul():
    def Mul_input(self, a, b):
            return a*b

class Div():
    def Div_input(self, a, b):
...             return a/b
... 
>>> class M(Plus,Minus,Mul,Div):
...     def start(self):
...             print('사용법')
...             print('더하기 = .Plus_input')
...             print('빼기 = .Minus_input')
...             print('곱하기 = .Mul_input')
...             print('나누기 = .Div_input')
... 
>>> x=M()
>>> x.start()
사용법
더하기 = .Plus_input
빼기 = .Minus_input
곱하기 = .Mul_input
나누기 = .Div_input
>>> x.Plus_input(10,10)
20
>>> x.Minus_input(20,10)
10
>>> x.Mul_input(5,4)
20
>>> x.Div_input(10,2)

>>> class Mul():
...     def Mul_input(self, a, b):
...             return a*b
... 
>>> class Div():
...     def Div_input(self, a, b):
...             return a/b
... 
>>> class M(Plus,Minus,Mul,Div):
...     def start(self):
...             print('사용법')
...             print('더하기 = .Plus_input')
...             print('빼기 = .Minus_input')
...             print('곱하기 = .Mul_input')
...             print('나누기 = .Div_input')
... 
>>> x=M()
>>> x.start()
사용법
더하기 = .Plus_input
빼기 = .Minus_input
곱하기 = .Mul_input
나누기 = .Div_input
>>> x.Plus_input(10,10)
20
>>> x.Minus_input(20,10)
10
>>> x.Mul_input(5,4)
20
>>> x.Div_input(10,2)


