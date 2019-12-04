# f = open("나없는파일",'r')
# # FileNotFoundError:[Errno 2]No such file or directory:"나없는파일"
# 4/0
# # IndexError: division by zero
# a=[1,2,3]
# a[4]
#indexError: list index out of range

#============= 오류 예외 처리 기법  =================
# try :
#   ...
# except [발생오류[as 오류 메시지 변수]]:
#   ...

#==============1. try, except만 쓰는 방법========================
# 이 경우는 오류 종류에 상관없이 오류가 발생하기만 하면 except 블록을 수행한다.

#==============2. 발생 오류만 포함한 except문 =========================
# 이 경우는 오류가 발생했을 때 except문에 미리 정해 놓은 오류 이름과 일치할 때만 
# except 블록을 수행한다

#==============3. 발생 오류와 오류 메시지 변수까지 포함한 except문 ================
# 이 경우는 두 번째 경우에서 오류 메시지의 내용까지 알고 싶을 때 사용하는 방법이다.
try:
    4/0
except ZeroDivisionError as e:
    print(e)

#============= try...else... =========================================
# else 절은 예외가 발생하지 않은 경우에 실행되면 반드시 except절 바로 다음에 위치
# 
try:
    f = open('foo.txt','r')
except FileNotFoundError as e:
    print(str(e))
else: 
    data = f.read()
    f.close()
    print(f)

#============= finally ================================================
f = open('foo.txt','w')
try:
    # 무언가를 수행한다.
finally:
    f.close()
#=========== 오류 패스하기 ===============================================
try:
    f = open("나 없는 파일", 'r')
except FileNOtFoundError:
    pass
# 오류가 발생 할 경우 회피하는 예제

#=========== 오류를 일부러 발생시키기 ====================================
class Bird:
    def fly(self):
        raise NotImplementedError # 꼭 작성해야 하는 부분이 구현되지 않았을 경우의 오류
