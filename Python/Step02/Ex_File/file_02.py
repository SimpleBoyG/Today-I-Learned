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
    