def hello():
    print('Hello, world!')
hello()

def test():
    print('Test Printing!!!')
test()

def Add(a,b):
    print(a+b)
    
def Minus(a,b):
    print(a-b)
    
Add(2,5)
Minus(4,6)

def not_ten(a):
    if a == 10:
        return 
    print(a,'number', sep='')
not_ten(10)
not_ten(1)

def not_ten2(a):
    if a == 10:
        print('Correct')
    else:
        print('Wrong')
    
not_ten2(10)
not_ten2(5)

def add_sub(a,b):
    return a+b, a-b

x, y = add_sub(10, 20)
print(x,y)

def divide(a,b):
    print(a/b)
    
def mul_div(a,b):
    c = divide(a,b)
    d = a*b
    return c,d
    
x, y = mul_div(10, 5)
print(x,y)

print()
def mod():
    print(10%3)
#=================Ex 나머지, 몫 구하기 ==================================    
def div_mod():
    c = mod()
    d = 10/3
    print(c)
    print(d)
    
div_mod()

def div(a,b):
    c,d = divmod(a,b)
    print('몫 = %d 나머지 = %d'%(c,d))
    return 0

#=================
def print_numbers(a,b,c):
    print(a)
    print(b)
    print(c)
    
print_numbers(10,29,30)

a=[231,33,21]
print_numbers(*a) # 언팩킹?

def pt_num(*args):
    for arg in args:
        print(arg)
        
b={0,1,2,3,4,5,6,7}
e = list(b)

pt_num(*e)


print("안녕")
