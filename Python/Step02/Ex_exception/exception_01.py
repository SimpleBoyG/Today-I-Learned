#=================== 예외 처리 =================================
# def ten_div():
#     try:
#         x = int(input('나눌 숫자를 입력하세요: '))
#         y = 10 / x

#         print(y)

#     except:
#         print('예외가 발생했습니다.')

# ten_div()

# y = [10,20,30]
# try:
#     index, x = map(int,input('인덱스와 나눌 숫자를 입력하세요: ').split())
#     print(y[index]/x)
# except ZeroDivisionError :
#     print('숫자를 0으로 나눌 수 없습니다.')
# except IndexError:
#     print('잘못된 인덱스 입니다.')

# ten_div()

#==================== 예외처리 에러메시지를 함께 출력 ========================
# y = [10,20,30]
# try:
#     index, x = map(int,input('인덱스와 나눌 숫자를 입력하세요: ').split())
#     print(y[index]/x)
# except ZeroDivisionError as e :
#     print('숫자를 0으로 나눌 수 없습니다.',e)
# except IndexError as e:
#     print('잘못된 인덱스 입니다.',e)


#============= 무조건 예외로 처리 =========================================
# y = [10,20,30]
# try:
#     index, x = map(int,input('인덱스와 나눌 숫자를 입력하세요: ').split())
#     print(y[index]/x)

# except Exception as e:
#     print('예외 처리 되었습니다.',e)

#============== else 사용 예외 ===========================================
# try:
#     x = int(input('나눌 숫자를 입려하세요'))
#     y = 10 / x
# except ZeroDivisionError:
#     print('숫자를 0으로 나눌 수 없습니다.')
# else:
#     print(y)

#============= finally 사용 ================================================
# try:
#     x = int(input('나눌 숫자를 입려하세요'))
#     y = 10 / x
# except ZeroDivisionError:
#     print('숫자를 0으로 나눌 수 없습니다.')
# else:
#     print(y)
# finally:
#     print('코드 실행이 끝났습니다.')

#================ 3의 배수가 아닙니다 ======================================
try:
    x = int(input('3의 배수를 입력하세요!!!!!'))
    if x % 3 != 0:
        raise Exception('3의 배수가 아닙니다')
    print(x)
except Exception as e:
    print('예외가 발생 했습니다.',e)

