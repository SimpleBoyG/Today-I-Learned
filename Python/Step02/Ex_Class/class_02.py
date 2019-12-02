#============각자의 가방에 넣기(이거 어려운데?) ============
class Person:
    
    def __init__(self):
        self.bag=[] # 값 초기화
        
    def put_bag(self, stuff): #가방에 넣는다
        self.bag.append(stuff)
    

jjs = Person()
jej = Person()

jjs.put_bag('money')
print(jjs.bag)
jej.put_bag('water')
print(jej.bag)