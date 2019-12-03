class A:
    def greeting(self):
        print('안녕하세요. A입니다.')

class B(A):
    pass
    # def greeting(slef):
    #     print('안녕하세요. B입니다.')
    
class C(A):
    pass
    # def greeting(self):
    #     print('안녕하세요. C입니다.')
    # C가 출력되었을 땐 C가 A보다 더 가깝다는 것을 알 수 있다

# class D(C, B): #C가 매개변수로 되어 먼저 출력된다
#     pass

# class D(B, C): #B가 매개변수로 되어 먼저 출력된다
#     pass

class D(B,C):
    pass

x = D()
x.greeting()

print(D.mro()) # 메소드를 실행하는 방식 및 순서를 보여준다

# class Point2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# p1 = Point2D(x=30, y=20)
# p2 = Point2D(x=60, y=50)
# print('p1: {} {}'.format(p1.x,p2.y))
# print('p2: {} {}'.format(p2.x,p2.y))

#==============삼각형의 길이를 계산해보자~~~~~~~~~=================
import math
class Point2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y
p1 = Point2D(x=30, y=20)
p2 = Point2D(x=60, y=50)

a = p2.x -p1.x
b = p2.y - p1.y
c = math.sqrt((a * a) + (b * b)) #제곱의 표현법
print("빗변의 길이는 = %d" %c)
c = math.sqrt(math.pow(a,2) + math.pow(b,2))
print("빗변의 길이는 = %d" %c)
d = math.sqrt((a**2) + (b**2))
print("빗변의 길이는 = %d" %c)

import collections

Point2D = collections.namedtuple('Point2D', ['x','y'])
p1 = Point2D(x = 30, y = 30)
p2 = Point2D(x = 60, y = 50)

a = p2.x -p1.x
b = p2.y - p1.y
c = math.sqrt((a * a) + (b * b)) #제곱의 표현법

d = math.sqrt((a**2) + (b**2))
print("빗변의 길이는 = %d" %c)
print()
