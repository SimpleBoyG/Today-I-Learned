#================== 배열 직접 입력 =========================
a = [[10,20],[30,40]]
b = a
b[0][0] = 600
print(b)

#================== 배열 복사 ==============================
b = a.copy()
print(b)

import copy
b = copy.deepcopy(a)
b[1][0] = 345
print(b)
print(a)

#================== 배열 모양으로 출력 ====================
i = 0
while i < len(a):
    j = 0
    while j < len(a[i]):
        print(a[i][j], end=' ' )
        j += 1
    print()
    i += 1

#=================== 3차원 배열 생성 ======================
a = []
for i in range(3):
    b = []
    for j in range(5):
        c = []
        for k in range(4):
            c.append(0)
        b.append(c)
    a.append(b)
print(a)  
#================== 3차원 배열 생성(한번에 선언) =======================  
a = []
b = []
c = []
for i in range(3):
    for j in range(5):
        for k in range(4):
            c.append(0)
        b.append(c)
    a.append(b)
print(a)
print(len(c))
#=================== 3차원 배열 생성1(한줄로)==============
a = [[[0 for k in range(4)] for j in range(5)] for i in range(3)]
print(a)
a = [[[0 for col in range(4)] for row in range(5)] for depth in range(3)]
print(a)
#=================== 3차원 배열 생성2(한출로)==============
a = [[[0] * i for i in [4,4,4,4,4]] * j for j in [1,1,1]]
print(a)
