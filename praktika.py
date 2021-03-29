# -*- coding: cp1251 -*-
"""
����� ����������� ��������� -2 + 3.5 * 2 - 3 ^ 2
"""

#������� ������� �� ������������
instr = input('��� ���������? ')
#instr = "-2 + 3.5 * 2 - 3 ^ 2"
print(instr)

#��������� ������ - strip ������� �� �����, a.replace('','') the best
# "-2 + 3.5 * 2 - 3 ^ 2"   ->    "-2+3.5*2-3^2"
instr = instr.replace(' ', '')



#����������
"""
�� ���� ������ 
"-2+3.5*2-3^2"

�� ����� ������ �������� � ���������� +-*/^ � �������

[{'opr': '', 'val': -2},{'opr': +, 'val': 3.5},{'opr': *, 'val': 2}, ...]

"""
# high priorities medium low, ����� tuple (), ����� ()
hp_ops = tuple('^')
mp_ops = ('*', '/')
lp_ops = tuple('+-')
# �������� �������� - �������� ���������� � ����
supported_ops = hp_ops + mp_ops + lp_ops
digit_chars = tuple('0123456789.-')

# () - ������� ��������, [] - ��������� �� �������������

actions = []
d = dict()
d['opr'] = 'First'
d['val'] = ''
actions.append(d)
# append ��������� ������� � ����� ������
print(actions)

# -2+3.5*2-3^-2
# [{'opr': '', 'val': '-2'},{'opr': +, 'val': '3.5'},{'opr': *, 'val': 2}, ...]
# �� ����� ������ � ���������� +-*/^ � �������

for i, letter in enumerate(instr):
    if letter in supported_ops and (i > 0) and actions[-1]['val'] != '':
        actions.append({'opr': letter, 'val': ''})

    elif letter in digit_chars:
        actions[-1]['val'] += letter

print(actions)

# ��������� �������� 1�� ���������� (���������� � �������)
"""
�� ���� ��� ����� �������� � ��������
�� ����� �������������� ���������

-2+3.5*2-3^2
-2+3.5*2-9
"""
i = 0
actions.reverse()
print(actions)
while i < len(actions):
    """��������� �������� � �������� �� ������������ �������� ������� ����������, 
    ���� ��� �� ��������������� , �� ������ �� ������, ���� ��� �����, ��
    ��������� ��������� ��� ����� � ���� �������� � ������ ������ � �������� ���-� � ������ ������,
    ������� ������� ��������
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


# ��������� �������� 2�� ���������� (����� � ���)
"""
�� ���� ��� ����� �������� � ��������
�� �����  ����������� ��������� ������

-2+3.5*2-9
-2+7-9
"""
i = 0
result = '0'
error = False
while i < len(actions):
    """��������� �������� � �������� �� ������������ �������� ������� ����������
    ���� ��� �� ��������������� , �� ������ �� ������, ���� ��� �����, �� 
    - ��������� ��������� ��� ����� � ���� �������� � ������ �����
    - � �������� ���-� � ������ �����
    - ������� ������� �������� 
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
#��������� �������� 3�� ���������� (�������� � ��������)
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
        
        
# ������� ��������� 
print('���������: {}'.format(result))