a = "Узун Дарья Сергеевна"
fio = a.split()

print('№1 ' + str(fio == ['Узун', 'Дарья', 'Сергеевна']))

name = fio[1]

print('№2 ' + str(name == 'Дарья'))

l = len(fio[0])
print('№3 ' + str(l == 4))

u = list('Узун')
res = u[2]

print('№4 ' + str(res == 'у'))

u = list('Узун')
res = u[0] + u[1]

print('№5 ' + str(res == 'Уз'))

u = list('Узун')
res = u[2] + u[3]
print('№6 ' + str(res == 'ун'))

surname_list = list('Узун')
print('№7 ' + str(surname_list == ['У', 'з', 'у', 'н']))

surname_tuple = tuple('Узун')
print('№8 ' + str(surname_tuple == ('У', 'з', 'у', 'н')))

res = list(range(len('Узун')))
res = res [2::2]

print('№9 ' + str(res == [2]))

res = list()
for i in enumerate(surname_list):
    res.append(tuple(i))
print('№10 ' + str(res == [(0, 'У'), (1, 'з'), (2, 'у'), (3, 'н')]))

res = list(reversed(surname_list))
print('№11 ' + str(res == ['н', 'у', 'з', 'У']))

res =''.join(reversed(fio[0]))
print('№12 ' + str(res == 'нузУ'))

surname_list = list('Узун')
surname_list.remove(surname_list[2])
res = surname_list
print('№13 ' + str(res == ['У', 'з', 'н']))
