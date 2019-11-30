a = [0,0,0,0,0,0]
b = a
print('1.')
print(b)

b[2] = 45
print('\n2.')
print(b)

print('\n3.')
for i in b:   
    print(i) 

print('\n4.')
a = [11,22,33,44,55,66,77]
for index, value in enumerate(a):
    print(index, value)
  
print('\n5.')   
for index, value in enumerate(a, start=1):
    print(index, value)
    
print('\n6.')
for index in range(len(a)):
    print(a[index])
    
#===============================================
print('\nEX 1.')
i=0
index = range(len(a))
while i in index:
    i+=1
    print(i)
    
# while i<7:
#     
#     print(a[i])
#     i=i+1
#     
#     if i==7:
#         break
    
   
    