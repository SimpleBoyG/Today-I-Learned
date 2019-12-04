#=================== 배열을 차례대로 출력 ==============================
# it = [23,13,45].__iter__()

# e = it.__next__()
# print(e)
# e = it.__next__()
# print(e)
# e = it.__next__()
# print(e)
# print()

#=================== 많은 배열을 차례대로 출력 =========================
# for i in range(10):
#     print(i)

    
# k = i.__next__()
# print(k)

#================= 문자열을 차례대로 출력 ==============================
# a = 'This, is a computer'.__iter__()
# str = a.__next__()
# print(str)

# str = a.__next__()
# print(str)

# str = a.__next__()
# print(str)

# str = a.__next__()
# print(str)

# str = a.__next__()
# print(str)

#================= dict를 차례대로 출력 ================================
# dict = {'참색' : '짹짹' , '고양이' : '먀옹~', '호랑이' : '냐옹냐옹', '병아리' : '뺴액~', '코끼리' : '멀미안뇽~'}.__iter__()
# dic = dict._next__()
# print(dic)

# dic = dict._next__()
# print(dic)

# dic = dict._next__()
# print(dic)

# dic = dict._next__()
# print(dic)

# dic = dict._next__()
# print(dic)

#===================== Ex(iter) =========================================
class Counter:
    def __init__(self, stop):
        self.current = 0
        self.stop = stop
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.stop:
            r =  self.current
            self.current += 1
            return r
        else : 
            raise StopIteration

for i in Counter(8):
    print(i, end=', ')

print('개수 출력')
a,b,c = Counter(3)
print(a,b,c)
print()

# 난수 출력
# print('난수 출력')
# import random
# it = iter(lambda: random.randint(0,5), 2)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print()


# ================정해진 난수 일 떄 반복 중지==============
print(' for문 사용 ')
import random
it = iter(lambda:random.randint(0,5),6)
for i in it:
    print(i)
    if i == 3:
        print('3이 출력되었습니다.')
        break
        
    
   
    

# # 범위 출력
# a, _, c =rang(3)
# print(next(a)
# print()
# it = iter(range(3))
# print('범위 출력')
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it,10))
# print()











