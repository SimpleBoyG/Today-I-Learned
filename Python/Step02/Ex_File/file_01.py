
file = open('Hello.txt', 'w') #파일을 열 때 w:쓰기 모드로 열기
file.write('Hello,World!!' 'Test with python.') #파일 쓰기
file.close() #파일 닫기

file = open('hello.txt','r') #파일을 열 때 r:읽기 모드로 열기
s=file.read() #파일을 읽는다
print(s)
file.close() #파일을 닫는다

file = open('Hello2.txt', 'w')
file.write('Hello, Python!!!!!' 'Wellcome to Python')
file.close()

f = open('Hello2.txt', 'r')
m=f.read()
print(m)
f.close()

#============
with open('test1.txt','w') as file:
    for i in range(3):
        file.write('Hello, world! {0}\n'.format(i))
file.close()

file = open('test1.txt','r')
h=file.read()
print(h)

file.close()
with open('test1.txt','r') as file:
    s = None
    while s != '' :
        s = file.readline()
        print(s.strip('\n')) # 한 줄씩 읽어 출력한다
        
