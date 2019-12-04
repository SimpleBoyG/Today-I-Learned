#=========== assert? if 대신? ======================================
# def three_multiple():
#     try:
#         x = int(input('3의 배수를 입력하세요'))
#         assert x % 3 == 0, '3의 배수가 아닙니다.'
#         print(x)
#     except Exception as  e:
#         print('three multiple 함수에서 예외가 발생 했습니다.',e)
#         raise #발생을 시킨다.

# try:
#     three_multiple()
# except Exception as e:
#     print('스크립트 파일에서 예외가 발생했습니다.')

#============ 3의 배수 에러 메시지 출력 후 다시 질문 출력 ====================================
# class NotThreeMultipleError(Exception):
#     def __init__(self):
#         super().__init__('3의 배수가 아닙니다.')
    
# def three_multi():
#     try:
#         x = int(input('3의 배수를 입력하세요'))
#         if x % 3 != 0:
#             raise NotThreeMultipleError
#         print()
#     except Exception as e:
#         print('예외가 발생 했습니다.',e)


# three_multi()


# 1. 샘플 파일을 만들고
# 2. 그 파일을 출력하고
# 3. 예외 처리를 하여라

file = open('sample.txt','w')
file.write('Hello,World!!' 'Test with python.')
file.close()

try:
    file = open('sample.txt','r')
except FileNotFoundError as e:
    print('파일이 없습니다.',e)
else:
    s = file.read()
    file.close()
    print(s)
finally:
    print('코드 실행이 끝났습니다.')