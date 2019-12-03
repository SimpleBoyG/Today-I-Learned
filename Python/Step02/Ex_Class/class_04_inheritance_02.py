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

