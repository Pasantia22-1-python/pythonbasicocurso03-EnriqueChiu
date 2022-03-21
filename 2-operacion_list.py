import random

a = list(range(0, 100, 2))
print(a)

b =list(range(0, 10))
print(b*2)
print(b*3)

# ERROR a/b 
# ERROR a%b
# ERROR a-b

print('*'*20+' apeend() '+'*'*20)
fruits = []
fruits.append('apple')
print(fruits)
fruits.append('banana')
print(fruits)
fruits.append('kiwi')
print(fruits)

print('*'*20+' pop() '+'*'*20)
some_fruits = fruits.pop()
print(some_fruits)
print(fruits)
some_fruits2 = fruits.pop(0)
print(some_fruits2)
print(fruits)

print('*'*20+' del '+'*'*20)
del fruits[0]
print(fruits)



print('*'*20+' random '+'*'*20)
list_random = []
for i in range(10):
    list_random.append(random.randint(0,15))
print(list_random)

print('*'*20+' sorted '+'*'*20)
order_list = sorted(list_random)
print(order_list)
print('*'*20+' sort '+'*'*20)
list_random.sort()
print(list_random)