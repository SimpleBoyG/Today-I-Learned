#=============== class가 필요한 이유? ====================================
# 기본 적으로 함수는 이렇게 사용된다
result = 0 

def adder(num):
    global result
    result += num
    return result

print(adder(3))
print(adder(4))

#==========만약 2개의 계산기가 필요할 경우에는? ============================
#========= 클래스가 없는 경우에는 다음과 같이 각 각 1개씩 만들어야 한다===================
result1 = 0
result2 = 0

def adder1(num): # 1번 함수
    global result1
    result1 += num
    return result1

def adder2(num): # 2번 함수
    global result2
    result2 += num
    return result2

print(adder1(3))
print(adder1(4))
print(adder2(3))
print(adder2(7))
print()
#====================클래스를 이용한다면? ===================================
class Calculator:
    def __init__(self):
        self.result = 0

    def adder(self, num):
        self.result += num
        return self.result
    
cal1 = Calculator() # cal1 인스턴스 생성
cal2 = Calculator() # cal2 인스턴스 생성
#인스턴스의 생성만으로도 각각의 독립적인 결과값을 유지한다
#계산기의 개수가 얼만큼 늘어나더라도 사용하기가 간단해진다

print(cal1.adder(3))
print(cal1.adder(4))
print(cal2.adder(3))
print(cal2.adder(7))
print()

#============ Class의 개념 잡기 ============================================
# 클래스는 설탕 뽑기의 틀?
# 인스턴스는 별모양 틀에서는 별모양이 하제모양에서는 하트모양이 나온다.

#========Exemple(간단한 예제) ==============================================
class Simple: # class 생성
    pass
a = Simple() # 심플모양의 인스턴스 생성

#여기서 잠깐! 객체와 인스턴스의 차이는?~~~~~~???????
# 클래스에 의해서 만들어진 객체를 인스턴스라고 한다. 그렇다면 객체와 인스턴스의 차이는 무엇일까?
# 이렇게 생각해 보자. navi = Cat() 이렇게 만들어진 navi는 객체이다. 그리고 navi라는 객체는 Cat의 
# 인스턴스이다. 즉, 인스턴스라는 말은 특정 객체(navi)가 어떤 클래스(Cat)의 객체인지를 관계 위주로
# 설명할 때 사용된다. 즉, 'navi는 인스터스' 보다는 'navi는 객체'라는 표현이 어울리며, 'navi는 Cat의 객체'
# 보다는 'navi는 Cat의 인스턴스'라는 표현이 훨씬 잘 어울린다.

#========================쉽게 설명해보자 ====================================
# 결국 클래스란건 혜택이라 볼 수 있다, 다음의 예를 보자

# 먼저 서비스를 제공한다.(클래스를 만든다.)
class Service: # 서비스를 만든다
    secret = "가입자들만 볼 수 있습니다." # 가입자들만 볼 수 있는 유용한 정보
    def sum(self, a, b): # 더하기를 해주는 서비스, self는 가입자인지 아닌지를 판단
        result = a + b
        print("%s + %s = %s입니다." %(a,b,result))

pey = Service() # 서비스 업체에 가입을 한다

pey.sum(1,1) # pey라는 이름으로 더하기 서비스를 사용한다
print(pey.secret) #pey라는 이름으로 유용한 정보 보기

#====== self는 왜 필요한가? ====================================================
# self라는 변수를 클래스 함수의 첫 번째 인수로 받는 것은 파이썬의 특징이다.
# 클래스 내 함수의 첫 번째 인수는 무조건 self로 사용해야 인스턴스의 함수로 사용할 수 있다.

#============= self 더 파헤치기 ==================================================
class Service1:
    secret = "가입자들만 볼 수 있습니다."
    def setname(self,name):
        self.name = name
    
    def sum(self,a,b):
        result = a + b       
        print("%s님 %s + %s = %s입니다." %(self.name, a, b, result)

pey = Service1()

pey.setname('정 준상 ')
pey.sum(1,1)
#결국 self는 가입자 본인의 계정인 pey가 들어갈 자리라고 보면 된다
print()
# ===============__init__ 이란 무엇인가?===================

# __init__ : 인스턴스를 만들 때 항상 실행된다

# class Service2:
#     secret = "가입자들의 유용한 정보"
#     def __init__(self, name):
#         self.name = name
#     def sum(self, a, b):
#         result = a + b
#         print("%s님 %s + %s = %s입니다." %(self.name, a, b, result))


    

