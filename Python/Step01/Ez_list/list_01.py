
a=[10,20,30]
a.append(500)
print('1.')
print(a)

print('\n2.')
print(len(a))

#=================================================
a.append([100, 200])
print('\n3.')
print(a)

a=[10,20,30]
a.extend([40, 50])
print('\n4.')
print(a)
 
a.insert(2,25)
print('\n5.')
print(a)
 
a[1:1] = [200, 300]
print('\n6.')
print(a)
 
a.pop()
print('\n7.')
print(a)

a.pop(1)
print('\n8.')
print(a)

del a[1]
print('\n9.')
print(a)

a.remove(25)
print('\n10.')
print(a)

a.count(20)
print('\n11.')
print(a)

a.reverse()
print('\n12.')
print(a)

a.sort()
print('\n13')
print(a)

a.clear()
print('\n14.')
print(a)




