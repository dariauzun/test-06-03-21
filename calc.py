#simple div

str_command = input("Please type command a + b or a-b")

sign_A = ''
str_A = ''

sign_B = ''
str_B = ''

operation = ''
i = 0

while i < len(str_command):
	if str_command[i] == '+' or str_command[i] == '-' or str_command[i] == '*' or str_command[i] == '/' or str_command[i] == '^':
		if str_A == '':
			sign_A = str_command[i]
		elif operation != '':
			sign_B = str_command[i]
		else:
			operation = str_command[i]
	else:
		if operation == '':
			str_A += str_command[i]
		else:
			str_B += str_command[i]
	i += 1

str_A = sign_A + str_A.strip()
str_B = sign_B + str_B.strip()
print(str_A)
print(str_B)


#str_input = input("A: ")

delimoe = float(str_A)
#print(type(delimoe))

#operation = input("+ / * - ^: ")

#str_input2 = input("B: ")
delitel = float(str_B)
#print(type(delitel))
result = None

if operation == '/':
	if delitel == 0:  
		result = 'Inf'
	else:
		result = delimoe / delitel
#print(type(result))
elif operation == '+':
 result = delimoe + delitel
elif operation == '-':
 result = delimoe - delitel
elif operation == '*':
 result = delimoe * delitel
elif operation == '^':
 result = delimoe ** delitel

else:
 result = "unknown"
#lol
#print(type(result))

print("Result: " + str(result))
print("Result: " + str(result))