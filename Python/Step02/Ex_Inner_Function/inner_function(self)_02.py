# 1. hex(x)
# 정수값을 입력받아 16진수(hexadecimal)로 변환하여 리턴하는 함수이다.
print('1.')
a = hex(345)
print(a)
a = hex(3)
print(a)
print()

# 2. id
# id(object)는 객체를 입력받아 객체의 고유 주소값(레퍼런스)을 입력하는 함수이다.
print('2.')
a = 3
b = a
print(id(3)) # 고유 주소값을 출력
print(id(a))
print(id(b))
# print(id(4)) 다른 객체이므로 오류 출력
print()

# 3. input([prompt])
# 사용자의 입력을 받는 함수이다.
print('3.')
# a = input("문장을 입력해주세요.\n")
# print(a) 
# b = input("숫자를 입력해주세요.\n")
# print(b)
print()

# 4. int 
# 정수로 출력
print('4.')
print(int(3.0))
print(int('55')) # 문자열 형태를 정수로 출력
print(int('11',2)) # 2진수로 표현된 1턴
print(int('1A', 16)) # 16진수로 표현된 1A
print()

# 5. isinstance(object, class)
# 첫 번째 인수로 인스턴스, 두 번째 인수로 클래스 이름을 받는다.
# 입력으로 받은 인스턴스가 그 클래스의 인스턴스인지를 판단하여 참이면 True, 것짓이면 False 리턴
print('5.')
class Person: pass # 아무 기능이 없는 class

a = Person() # Person의 인스턴스 생성
print(isinstance(a,Person)) # a가 Person의 인스턴스 인지 확인 후 판단
b = 3
print(isinstance(b,Person)) # b는 Person의 인스턴스가 아니다.
print()

# 6. lambda 인수1, 인수2, ... : 인수를 이용한 표현식
# 함수를 생성할 때 사용하는 예약어
# def와 동일한 역할을 한다.
# 보통 함수를 한 줄로 간결하게 만들 때 사용한다.
# def를 사용 할 수 없는 곳에 주로 쓰인다.
print('6.')

# lambda를 이용한 표현
sum = lambda a,b: a+b
sum(3,4)

# def 함수를 이용한 표현
def sum1(a,b):
    return a+b
# 그럼 왜 def가 있는 lambda를 사용하는 것일까???
# 1. lambda는 def 보다 간결하게 작성이 가능하다.
# 2. def를 사용할 수 없는 곳에도 사용할 수 있다.
myList = [lambda a,b:a+b, lambda a,b:a*b]
print(myList)
a = myList[0]
print(a)
a = myList[0](6,7)
print(a)
print()

# 7. len(s), s = 길이(요소의 전체 개수)
print('7.')
print(len("python"))
print(len([1,2,3]))
print(len((1,'a'))) # 두 개라서 그런가...?
print()

# 8. list(s), s = 반복 가능한 자료형
print('8.')
print(list("python"))
print(list((1,2,3)))
print()

# 9. map(f, iterable)
# 함수(f)와 반복 가능한(iterable) 자료형을 입력으로 받는다.
# map은 입력 받은 자료형의 각 요소가 f에 의해 수행된 결과를 묶어서 리턴하는 함수이다.

#[본 코드]
print('9.')
def two_times1(numberList):
    result = []
    for number in numberList:
        result.append(number*2)
    return result

result = two_times1([1,2,3,4])
print(result)

# map 사용
def two_times2(x): return x*2
    
a = list(map(two_times2, [1,2,3,4]))
print(a)

# lambda 사용
a = list(map(lambda a: a*2, [1,2,3,4]))
print(a)

# Another Exemple
def plus_one(x):
    return x+1
a = list(map(plus_one, [1,2,3,4,5]))
print(a)
print()

# max(iterable)
# 인수로 반복 가능한 자료형을 입력받아 그 최대값을 출력하는 함수
print('10.')
print(max([1,2,100]))
print(max('python'))
print()

# min(iterable)
# 최소값을 출력
print('11.')
print(min([1,2,100]))
print(min("python"))









