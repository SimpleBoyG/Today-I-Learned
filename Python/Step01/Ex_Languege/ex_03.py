x = 10
if x==10:
    print('x is ', end='');print(x) # 불필요
    
    
a = 12.34
b = 23.4
c = -3.54
if a < b :
    print(b-a, end='')
    print('a = ', end='')
    print('b = ', end='')
    print('difference is ', end ='')
    print(b-a)
    
if a > c :
    print('a is ', end ='')
    print(a-c, end = '')
    print('much more higher then ', end = '')
    print(' value of c.')
    
x = 3
if x > 6:
    print('x is more then 6.')
if x < 6:
    print('x is less then 6.')
    
for i in range(0, 10, 2):
    print('Hello, world!', i)
    
for i in range(10):
    print(i, end='') # 수평 처리
    
for i in range(10, 0, -2):
    print('Hello, World!', i)
    
h=('정준상','정준상2','정준상3','정준상4','정준상5')
d=('정준상','정준상2','정준상3','정준상4')
f=('정준상','정준상2','정준상3')

#============= 오호!=============================
for i in range(len(h)):
    print(h[i])
    
#================================================
fruits = ('apple', 'orange', 'grape')
for fruit in fruits:
    print(fruit)
    
    
 
    
 
    
    
    
    
    
