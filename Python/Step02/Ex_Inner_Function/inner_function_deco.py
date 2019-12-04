# class Calc:
#     @staticmethod
#     @classmethod
#     @abstractmethod
#     def add(a,b):
#=============== Deco ======================
# def trace(func):
#     def wrapper():
#         print(func.__name__, '함수 시작')
#         func()
#         print(func.__name__, '함수 끝')
#     return wrapper

# def hello():
#     print('hello')

# def world():
#     print('world')

# trace_hello = trace(hello)
# trace_hello()
# trace_world = trace(world)
# trace_world()

#================??????===============================
def trace(func):
    def wrapper():
        print(func.__name__, '함수 시작')
        func()
        print(func.__name__, '함수 끝')
    return wrapper

@trace
def hello():
    print('hello')

@trace
def world():
    print('world')

hello()
world()

#=============??????????????????????=====================
def deco1(func):
    def wrapper():
        print('데코레이터1')
        func()
    return wrapper

def deco2(func):
    def wrapper():
        print('데코레이터2')
        func()
    return wrapper

@deco1
@deco2

def hello():
    print('hello')

e = hello()
print(e)

#====================???????????????????===================


