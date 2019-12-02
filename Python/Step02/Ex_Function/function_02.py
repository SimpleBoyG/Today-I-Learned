def print_numbers(*args): # 언 패킹~
    for arg in args:
        print(arg)
a = [11,22,33,44,55,66,77,88,99,0]
print_numbers(*a)

#============== 딕셔너리 언패킹 =====================
def personal_info(name, age, address):
    print('이름 : ', name)
    print('나이 : ', age)
    print('주소 : ', address)
x = {'name':'홍길동', 'age':'30', 'address':'서울시 용산구 후암동'} #선언 전,후 는 상관이 없다.
personal_info(**x)
print()

#딕셔너리는 key-value쌍 형태로, 값이 저장 됨으로 *를 두 번 넣어 키와 값 모두를 언패킹한다.
#즉, **언패킹(*이 2개)은 딕셔너리에만 사용.

#=============== 키워드 인수를 사용하는 가변인수 함수 만들기 ==========================
def personal_info(**kwargs):
    for kw, arg in kwargs.items():
        print(kw, ':',arg,sep='')
personal_info(name='홍길동')
print()
personal_info(name='홍길동',age = 30, address = '서울시 동작구 상도동')
print()

def jjs_list(**value):
    for k1,k2 in value.items():
        print(k1, ':', k2,sep='')
jjs_list(name='정준상')
jjs_list(name='정준상', age = "29", address = '금천구 가산동' , hobby ='운동, 게임', 스펙 = '토익', 성격 = '괴팍함')
print()
#==========여러 파일의 문장 불러오기(미완) ======================================
# kw1 = ['name 정준상']
# kw2 = ['age 29세']
# kw3 = ['address 나 서울사람이야~']
# with open('k1.text','w') as jjs_file:
#     jjs_file.writeline(kw1)
#     jjs_file.writeline(kw2)
#     jjs_file.writeline(kw3)

# def personal_info(name, age, address):
#     print('이름 : ', name)
#     print('나이 : ', age)
#     print('주소 : ', address)
    


# def jjs_list2(**k1):
#     for t1,t2 in k1.items():
#         print(t1,':',t2,sep='')

# with open('k1.txt','r') as jjs_file:
#     lines = jjs_file.readlines()
#     print(lines)
#     print()
#========== Custom print함수 만들기 ===============================
def custom_print(*args, **kwargs):
    print(*args, **kwargs)
    print()
    print()
   
custom_print(1,2,3, sep=':',end='')

print(1,2,3, sep=':',end='')
print()
print()
#===================재귀호출========================================

def factorial(n): #팩토리얼
    if n==1:
        return 1
    return n*factorial(n-1)

print(factorial(5))
print()

#============= 람다 표현식 ========================================
plus_ten = lambda x: x+10
plus_ten(1)
print(plus_ten(1))
# 식 한줄로 표현할 수 있는 단일 변수에 대한 표현법
# (2변수 이상 만들경우는 def를 이용하여야 한다.)

#======== lambda함수를 map함수에 적용하기 ==========================
a = list(range(1,11))
print(a)
print()
b = list(map(lambda x: str(x) if x%3 == 0 else x,a))
print(b)
print()
c = list(map(lambda x: str(x) if x==1 else float(x) if x==2 else x+10,a))
print(c)
print()

#============ 람다 표현식을 filter에 적용하기(미완) =======================
def filter_ex(x):
    return x > 10 and x < 1

d = list(range(1,20))
print(d)
list(filter(filter_ex,d))
list(filter(lambda x: x>5 and x<10,d))
#================Reduce 사용하기 ===========================================
def f(x,y):
    return x+y
from functools import reduce #추가해야만 사용가능
a = list(range(1,6))
print(a)
reduce(f,a)
# reduce함수를 사용하기 위해서는 function함수로부터 가져와야 한다.
# 같은 효과를 얻기 위해 람다 표현식으로 사용할 수 있습니다.
# reduce(lambda x,y:x+y,a)

#=============== closure 사용하기 -1. 변수 사용 범위 ========================
# #글로벌변수
# x=10
# def foo():
#     print(x)

# foo()
# print(x)
# print()
# #로컬변수
# x=''
# def foo():
#     x=10
#     print(x)

# foo()
# print(x)

#============= Closure 사용하기 - 2.함수안에서 전역변수 변경하기(미완) ==============
# def foo():
#     global x
#     x=20
#     print(x)
# 완
# x=45
# print(x) # 변경 전 전역변수
# foo()
# print(x) # 변경 후 전역변수



#============= Closure 사용하기 -3. nonlocal의 적용 범위(미완) ======================
# def A():
#     x=10
#     def B():
#         nonlocal x
#         x=20
#     B()
#     print(x)
# A()

# def A():
#     x=10
#     y=100
#     def B():
#         x=20
#         def C():

#============ Closure 사용하기 -4. global은 항상 적용 ======================
#============ Closure 사용하기 -5. Closure 함수 구성 =======================
#============ Closure 사용하기 -6. Closure 함수의 지역변수 변경하기==========
print('nonlocal')

def calc_ex():
    a=3
    b=5
    total=0
    def mul_add(x):
        nonlocal total
        total = total + a*x + b
        print(total)
    return mul_add

e=calc_ex()
print(e(5))
print(e(5))
print(e(5))

