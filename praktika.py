# -*- coding: cp1251 -*-
"""
хотим калькулятор выражений -2 + 3.5 * 2 - 3 ^ 2
"""

#считать строчку от пользователя
instr = input('Что вычислить? ')
#instr = "-2 + 3.5 * 2 - 3 ^ 2"
print(instr)

#почистить строку - strip убирает по краям, a.replace('','') the best
# "-2 + 3.5 * 2 - 3 ^ 2"   ->    "-2+3.5*2-3^2"
instr = instr.replace(' ', '')



#распарсить
"""
на вход строку 
"-2+3.5*2-3^2"

на выход список словарей с операциями +-*/^ и числами

[{'opr': '', 'val': -2},{'opr': +, 'val': 3.5},{'opr': *, 'val': 2}, ...]

"""
# high priorities medium low, можно tuple (), можно ()
hp_ops = tuple('^')
mp_ops = ('*', '/')
lp_ops = tuple('+-')
# название операций - операции запихуемые в тупл
supported_ops = hp_ops + mp_ops + lp_ops
digit_chars = tuple('0123456789.-')

# () - цельное значение, [] - разбивает на составляеющие

actions = []
d = dict()
d['opr'] = 'First'
d['val'] = ''
actions.append(d)
# append добавляет элемент в конец списка
print(actions)

# -2+3.5*2-3^-2
# [{'opr': '', 'val': '-2'},{'opr': +, 'val': '3.5'},{'opr': *, 'val': 2}, ...]
# на выход список с операциями +-*/^ и числами

for i, letter in enumerate(instr):
    if letter in supported_ops and (i > 0) and actions[-1]['val'] != '':
        actions.append({'opr': letter, 'val': ''})

    elif letter in digit_chars:
        actions[-1]['val'] += letter

print(actions)

# вычислить операции 1го приоритета (возведение в степень)
"""
на вход наш набор значений и операций
на выход промеждуточный результат

-2+3.5*2-3^2
-2+3.5*2-9
"""
i = 0
actions.reverse()
print(actions)
while i < len(actions):
    """проверить операции в действии на соответствие операции первого приоритета, 
    если она не осообтветствует , то ничего не делаем, если она соотв, то
    вычисляем результат для числа в этом действии и соседа справа и записать рез-т в соседа справа,
    удалить текущее действие
    """
    action = actions[i]
    operation = action.get('opr')
    if operation in hp_ops:
        if operation == '^':
            pre_res = float(actions[i+1].get('val')) ** float(action.get('val'))
            actions[i+1]['val'] = str(pre_res)
            del actions[i]
    else:
        i += 1
actions.reverse()


# вычислить операции 2го приоритета (умнож и дел)
"""
на вход наш набор значений и операций
на выход  обновленная структура данных

-2+3.5*2-9
-2+7-9
"""
i = 0
result = '0'
error = False
while i < len(actions):
    """проверить операции в действии на соответствие операции второго приоритета
    если она не осообтветствует , то ничего не делаем, если она соотв, то 
    - вычисляем результат для числа в этом действии и соседа слева
    - и записать рез-т в соседа слева
    - удалить текущее действие 
    """
    action = actions[i]
    operation = action.get('opr')
    if operation in mp_ops:
        if float(action.get('val')) == 0 and operation == '/':
            result = 'Inf'
            error = True
        else:
            eval_str = (actions[i-1].get('val') + operation + action.get('val'))
            pre_res = eval(eval_str)
            actions[i-1]['val'] = str(pre_res)
        actions.pop(i)
    else:
        i += 1
print(actions)
#вычисляем операции 3го приоритета (сложение и вычитаие)
# -2+7-9 = -4
if not error:
    for action in actions:
        var_A = result
        var_B = action.get('val')
        operation = action.get('opr')
        if operation in lp_ops:
            result = str(eval(var_A + operation + var_B))
        else:
            result = var_B
        print(result)
        
        
# вывести результат 
print('Результат: {}'.format(result))