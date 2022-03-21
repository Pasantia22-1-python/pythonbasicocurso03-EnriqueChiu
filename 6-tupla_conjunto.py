a = {1,2,3}
b = {3,4,5}

print(a.difference(b))
print(b.difference(a))

a = 1, 2, 3
print(type(a))
a = (1, 2, 3)
print(type(a))
print(a[0])
print(a[1])
print(a[2])

# ERROR a[0] = 10
print('*'*20+' count() '+'*'*20)
a = (1, 1, 1, 2, 3, 4)
print(a.count(1))
print(a.count(2))

print('*'*20+' index() '+'*'*20)
print(a.index(1))
print(a.index(3))


print('*'*20+' set() '+'*'*20)
a = set([1, 2, 3])
b = {3, 4, 5}
print(type(a))
print(type(b))

#ERROR INDEX => a[0]

print('*'*20+' add() '+'*'*20)
a.add(3) #no duplic
print(a)
a.add(20)
print(a)

print('*'*20+' interserction, union, difference '+'*'*20)
print(a.intersection(b))
print(a.union(b))
print(a.difference(b))
print(b.difference(a))

print('*'*20+' remove '+'*'*20)
a.remove(20)
print(a)