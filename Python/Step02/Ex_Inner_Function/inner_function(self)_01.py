# 1. abs (절대값)
print(abs(-3.2))
print('= 1')
print() 

# 2. all(x), 반복 가능한 자료형 x
# x가 모두 참이면 True, 거짓이 하나라도 있으면 False

a = all([1,2,3]) #리스트 자료형[1,2,3]은 모든 요소가 참
print(a)

a = all([1,2,3,0]) #요소 0은 거짓
print(a)
print('= 2')
print()

# 3. any(x)
# x 중 하나라도 참이 있을경우 True, x가 모두 거짓일 경우에만 False 
a = any([1,2,3,0]) # 참
print(a)
a = any([0, ""])
print(a)
print('= 3')
print()

# 4. chr(i) 
# 아스키(ASCII) 코드값을 입력으로 받아 그 코드에 해당하는 문자 출력
a = chr(97)
print(a)
a = chr(48)
print(a)
print('= 4')
print()

# 5. dir
# 객체가 자체적으로 가지고 있는 변수나 함수를 보여준다.
print(dir([1,2,3]))
print()
print(dir({'1':'a'}))
print('= 5')
print()

# 6. divmod(a,b)
# 2개의 숫자를 입력으로 받으며 a를 b로 나눈 몫과 나머지를 튜플 형태로 리턴
a = divmod(7,3)
print(a)
a = divmod(1.3, 0.2)
print(a)
print('= 6')
print()

# 7. enumerate
# '열거하다'라는 뜻이며 이 함수는 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력받아 
# 인덱스 값을 포함하는 enumerate객체를 리턴한다. 보통 for문과 같이 사용된다.
for i, name in enumerate(['body','foo','bar']):
    print(i,name)
print('= 7')
print()

# 8. eval
# eval(expression)은 실행 가능한 문자열을 입력으로 받아 문자열을 실행한 결과값을 리턴
# 결과값을 그대로 출력하기에 되도록 사용을 권장하지 않는다.
a = eval('1+2')
print(a)

a = eval("'hi' + 'a'")
print(a)

a = eval('divmod(4,3)')
print(a)

print('= 8')
print()

# filter(함수이름,반복가능 자료형)
# 두 번쨰 인수인 반복가능한 자료형 요소들이 첫 번째 인수인 함수에 입력되었을 때 
# 리턴값이 참인 것만 묶어서 돌려준다.

#[본 코드]
def positive(numberList):
    result = []
    for num in numberList:
        if num > 0:
            result.append(num)
    return result

print(positive([1, -3, 2, 0, -5, 6]))

#[filter 사용]
def positive1(x):
    return x > 0
    
print(list(filter(positive1,[1, -3, 2, 0, -5, 6])))
# lambda 사용
print(list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6])))

print('= 9')
print()


