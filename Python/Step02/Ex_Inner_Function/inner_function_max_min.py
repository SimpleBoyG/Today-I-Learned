#============== max min ==================
#============== trace ===================
#============ deco Multi ==============================================================

import functools
def is_multiple(x):
    def real_decorator(func):
        @functools.wraps(func)
        def wrapper(a,b):
            r = func(a,b)
            if r % x == 0:
                print('{0}의 반환값은 {1}의 배수 입니다.'.format(func.__name__,x))
            else:
                print('{0}의 반환값은 {1}의 배수가 아닙니다.'.format(func.__name__,x))
            return r
        return wrapper
    return real_decorator

@is_multiple(7)
@is_multiple(3)
def add(a, b):
    return a + b

print(add(10, 20))
print(add(2, 5))

#============== deco class ==============================================================
class Trace:
    def __init__(self,func):
        self.func = func
    def __call__(self):
        print(self.func.__name__, ' 함수 시작')
        self.func()
        print(self.func.__name__, ' 함수 끝')

@Trace
def hello():
    print('hello')

hello()


