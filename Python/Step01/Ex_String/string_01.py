#====================== 문자 바꾸기 =========================
from cmath import pi
a = 'Hello, World!!'
print(a)
a = a.replace('World!!', 'python') #초기화 해줄 것!!!!!!!!!!!
print(a)
b = a.replace('World!', 'test')
print(b)
print()
#======================번역으로 바꾸기=======================
table = str.maketrans('aeiou', '12345')
print(table)
'apple'.translate(table)
print(table)
print()
#===================== join으로 배열을 한번에 출력하기=========
a = 'apple pear grape pineapple orange test'
b = a.split()
print(b)
print('-'.join(b))
print()
#===================대,소문자 바꾸기==========================
print(a.upper())
print(a.lower())
b = a.upper()
b = a.lower
print()
#==================== 자르기 =================================
a = '        ,,,        python   ...             '
b = a.lstrip() #왼쪽 공백 자르기
print(b)
c = a.rstrip() #오른쪽 공백 자르기
print(c)
d = a.strip()
print(d) #모든 공백 자르기

#공백과 점을 지우기
import string
print(' ,   python ......'.strip(string.punctuation + ''))
print()
#=========원하는 정렬 설정하기 ============================
print('python'.ljust(10)) #10칸중에서 왼쪽정렬
print('python'.rjust(10))
print('python'.center(10))
print('python'.center(10).upper())
print()
#======================= 빈 공간 0으로 채우기 ============================
print('35'.zfill(4))
print('3.5'.zfill(7)) #zorofill
print()
#================= 원하는 글자 위치를 알려주기 ======================
a.find('pi')
a.find('xy')
a.rfind('pi')
a.rfind('or')
print()
#=====================글자의 개수를 알려주기============================
a.count('a') # a라는 글자가 문장에 몇 개 들어있는지 알려준다.
print()
#===================== 문자열 집어넣기 ================================
# 문자열
print('This is a %s' %'Ubuntu')

# 숫자
print('This year is %d' % 2019)
print('The weight is %f.' % 34.5)
print('The weight is %.2f.' % 34.5) # 소수 두번째
print('The weight is %.3f.' % 34.5) # 소수 세번째
print('The weight is %.4f.' % 34.5) # 소수 네번째

# 여러개 대입
print('This year of %d rate is %.3f.' % (2019, 34.5))
x = 2020
y = 67.5
print('This year of %d rate is %.3f.' % (x, y))









