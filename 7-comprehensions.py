import random

list_num = list(range(100))

pares = [numero for numero in list_num if numero%2 == 0]
print(pares)

student_uid = [1, 2, 3]
students = ['Julio', 'David', 'Enrique']

students_with_uid = {uid: student for uid, student in zip(student_uid, students)}
print(students_with_uid)

list_random = []

for i in range(10):
    list_random.append(random.randint(1, 3))

print(list_random)
no_repeated = {number for number in list_random}
print(no_repeated)