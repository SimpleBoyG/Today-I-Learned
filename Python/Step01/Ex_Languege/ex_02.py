a = [1,2,3]
b = [4,5,6]
c = a+b
print(c)

a = (1,2,3)
b = (4,5,6)
c = a+b
print(a+b)

# 7 번 째의 글자를 출력하기
hello = "according to old saying, great hope make great man"
a=list(hello)
print(a)
print(a[7])
print(len(hello))

# 인덱스
a=[0,0,0,0,0]
a[0] = 11
a[1] = 22
a[2] = 33
a[3] = 44
a[4] = 55
print(a) 

# 튜플 인덱싱
b = tuple(range(0,300,7))
print(b)
print(b[0])
print(b[3:8]) # 3~8번 째 까지의 수를 출력
len(b) # 문자열의 길이를 출력
print(b[42])
print(b[35:])# 35번 째 이후로 모두 출력
print(b[-1]) # 42번 째 출력
print(b[-10]) # 리버스 10번 째 출력
print(b[-42]) # 리버스 42번 째 출력
print(b[:7:2]) # 0 부터 7번째 까지 숫자를 출력 후 2개의 간격으로 출력

s = slice(4,8) # s에 4~8번 째 까지의 배열을 저장
print(b[s])

#============== 예제 1 ==========================
c = list(range(0,40,2))
print(c)
h = c[2:7]
print(h)
h[0] = '즐'
h[1] = '거'
h[2] = '운'
h[3] = '수'
h[4] = '업'
print(h)
c[0:5] = h[0:5]
print(c)
#============== 풀이 =============================
m=list(range(0,40,2))
for i in range(len(m)):
    if(i>=3 and i <=7):
        m[i] = 'a'
print(m)    
#============== 응용 =============================   
d = list(range(0,40,2))
for i in range(len(d)):
    m[3] = '즐'
    m[4] = '거'
    m[5] = '운'
    m[6] = '수'
    m[7] = '업'
print(m)

#=================================================
del c[10:len(c)] # 10번 째 부터 c 길이 번째 까지 삭제
print(c)

#=======딕셔너리 일반 방법 ===========================================================
lux = {'heat':490,'weight':330,'length':230,'data':123.4,'pi':3.141592} # key : value
print(lux)
print(lux['heat'])
print(lux['pi'])
lux['length']=445
print(lux['length'])
#======= dict을 사용한 방법 ===========================================================
lux1 = dict(heat = 490, weight = 330, length = 230, data = 123.4, pi = 3.141592)
print(lux1)
lux2 = dict(zip(['heat','weight','length','date','pi'],[490,330,230,123.4,3.141592]))
print(lux2)
        
        
        
        
        
        
        
        
        
        
        
        
        