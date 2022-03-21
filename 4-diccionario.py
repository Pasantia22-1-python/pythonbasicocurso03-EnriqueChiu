rae = {}
print('*'*20+" ASIGNACION DICT "+'*'*20)
rae['pizza'] = 'La comida mas deliciosa del mundo'
print(rae)
rae['pasta'] = 'La comida mas sabrosa de italia'
print(rae)

print('*'*20+" VALUE DICT "+'*'*20)
print(rae['pizza'])
print(rae['pasta'])
# ERROR KEY => print(rae['helado'])

print('*'*20+" GET DICT "+'*'*20)
a = rae.get('helado', None)
print(a)
a = rae.get('pizza', None)
print(a)


print('*'*20+" KEY DICT "+'*'*20)
print(rae.keys())

print('*'*20+" VALUES DICT "+'*'*20)
print(rae.values())

print('*'*20+" ITEM DICT "+'*'*20)
print(rae.items())


print('*'*20+" FOR DICT "+'*'*20)
print('*'*20+" KEY FOR "+'*'*20)
for key in rae.keys():
    print(key)

print('*'*20+" VALUE FOR "+'*'*20)
for value in rae.values():
    print(value)

print('*'*20+" ITEMS FOR "+'*'*20)
for key, value in rae.items():
    print(key, value)