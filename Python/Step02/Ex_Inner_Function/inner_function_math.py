import math
print("1.")
a = math.pi # 직접적으로 접근하여 값을 얻는 것, staticmethod
print(a) 
print()

import math as m
print("2.")
a = m.pi
print(a) 


a = m.sqrt(4.0)
print(a)
print()

#============== 필요한 함수만 호출하기 ===================
from math import pi # math의 많은 함수중 pi만 불러온다
print("3.")
print(pi)

from math import sqrt
print(sqrt(9.0))
print()

#============= 두개 이상 호출하기 ====================
from math import pi, sqrt
print("4.")
print(pi)
print(sqrt(3.4))
print()

#================ AS =================================
from math import pi as p, sqrt as s
print("5.")
print(p)
print(s(3.4))
print()
#======================== URL 호출하기 ==========================
print("6.")
import urllib.request
response = urllib.request.urlopen('http://www.google.com')
a = response.status # 200 = 요청 정상 처리
print(a)

import urllib.request as r
response = r.urlopen('http://www.google.com')
a = response.status
print(a)


from urllib.request import Request as r, urlopen as uopen
req = r('http://www.google.com') # URL에 요청해라
response = uopen(req) # URL을 열어 응답을 받아라
a = response.status
print(a)
print()

#=============== *을 사용하여 임폴트 =======================
print("7.")
from urllib.request import*
req = Request('http://www.google.com') # URL에 요청해라
response = urlopen(req) # URL을 열어 응답을 받아라
a = response.status
print(a)

#============== 파이썬 라이브러리 추가하기 ================
# 1. PSL
# curl -0 https://bootsrap.pypa.io/get-pip.py
# 2. PyPI
#=========================================================
r = requests.get('https://www.google.com')
a = r.status_code
print(a)

