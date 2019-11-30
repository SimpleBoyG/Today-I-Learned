# for i in range(1,101):
#     print('abc'+'def')
#     print((i%3 == 0)*(i%5==0))
#     print('abc'+'def'or i)
    
# for i in range(1,101):
#     print('abc'+'def\n',((i%3==0)*(i%5==0)),'\nabc'+'def' or i)
    

#==========동일한 결과값 얻기 ============================
# for i in range(1,101):
#     if i % 3 == 0 and i % 5 == 0:
#         print('Both')
#     elif i % 3 == 0:
#         print('three')
#     elif i % 5 == 0:
#         print('five')
#     else:
#         print(i)
#================ Print의 여러 형태 =======================
i=1
print('abc' * (i == 1))
print('abc' * (i != 1))
print('abc' * (i != 1) or i)
print('abc' * (i == 1) and i)
# for i in range(1,101):
#     print('three'*(i % 3 == 0) + 'five'*(i % 5 == 0) or i)