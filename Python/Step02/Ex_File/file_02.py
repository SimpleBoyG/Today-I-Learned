import pickle
name = 'Terry'
age = 15
address = 'Seoul Secho-Gu Banpo-Dong'
scores = {'Korean':90, 'english':92, 'math':93, 'science':91}
with open('terry.p','wb') as file:
    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(scores, file)

with open('terry.p','rb') as file:
    name = pickle.load(file)
    age = pickle.load(file)
    address = pickle.load(file)
    scores= pickle.load(file)
    print('Name : ', name)
    print('Age : ', name)
    print('Address : ', address)
    print('Scores : ', scores)

lines = ['안녕하세요.\n','파이썬 과정\n','수업 입니다.\n']

with open('hello.txt','w') as file:

    file.writelines(lines) #파일에 lines를 쓴다

with open('hello.txt','r') as file:
    lines = file.readlines() # 전체를 읽는다.
    print(lines)

with open('hello.txt','r') as file:
    line = None
    while line != '': # 공백이 나오면 멈춰라
        line = file.readline() # 한 줄 씩 읽어간라
        print(line.strip('\n'))

# /r : (Carriage Return)캐럿을 그 줄 맨 처음으로 이동한다.end
# /b : 

print('test1')
print('test2\n')
print('test3\r')


