a = "���� ����� ���������"
fio = a.split()

print('�1 ' + str(fio == ['����', '�����', '���������']))

name = fio[1]

print('�2 ' + str(name == '�����'))

l = len(fio[0])
print('�3 ' + str(l == 4))

u = list('����')
res = u[2]

print('�4 ' + str(res == '�'))

u = list('����')
res = u[0] + u[1]

print('�5 ' + str(res == '��'))

u = list('����')
res = u[2] + u[3]
print('�6 ' + str(res == '��'))

surname_list = list('����')
print('�7 ' + str(surname_list == ['�', '�', '�', '�']))

surname_tuple = tuple('����')
print('�8 ' + str(surname_tuple == ('�', '�', '�', '�')))

res = list(range(len('����')))
res = res [2::2]

print('�9 ' + str(res == [2]))

res = list()
for i in enumerate(surname_list):
    res.append(tuple(i))
print('�10 ' + str(res == [(0, '�'), (1, '�'), (2, '�'), (3, '�')]))

res = list(reversed(surname_list))
print('�11 ' + str(res == ['�', '�', '�', '�']))

res =''.join(reversed(fio[0]))
print('�12 ' + str(res == '����'))

surname_list = list('����')
surname_list.remove(surname_list[2])
res = surname_list
print('�13 ' + str(res == ['�', '�', '�']))
