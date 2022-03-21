import copy
from tkinter.messagebox import NO

countries = ['Mexico', 'Guatemala', 'Colombia', 'Venezuela']
ages = [12, 18, 24, 34, 50]

print("id(countries) => {}".format(id(countries)))
print('id(ages) => {}'.format(id(ages)))


weights = [12, 18, 24, 34, 50]
print('id(ages) => {}'.format(id(ages)))
print('id(weights) => {}'.format(id(weights)))

receta = ['Ensalada', 2, 'lechuga', 5, 'jitomates']

print("*"*20+" List is Mutable "+"*"*20)
print(countries)
countries[0] = 'Ecuador'
print(countries)

global_countries = countries

print("*"*20+" Change "+"*"*20)
countries[0] = 'Belice'
print(countries)
print(global_countries)

print("*"*20+" Copy() "+"*"*20)
global_countries = None
global_countries = copy.copy(countries)
print(global_countries)
print("*"*20+" Change "+"*"*20)
countries[0] = 'Honduras'
print(global_countries)
print(countries)


print("*"*20+" for list "+"*"*20)
for country in countries:
    print(country)




