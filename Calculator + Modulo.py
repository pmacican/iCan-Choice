num1 = int(input("Input the first number."))
num2 = int(input("Input the second number."))
operator = input("Which operation would you like to perform? +, -, /, *")

if operator == '+':
 print(num1 + num2)
elif operator == '-':
 print(num1 - num2)
elif operator == '/':
 if num2 != 0:
    print(num1 / num2)
 else:
    print("The second number cannot be 0.")
elif operator == '*':
 print(num1 * num2)
else:
 print("Invalid operator")


num1 = int(input("Input a number"))
num2 = int(input("Input another number"))

if (num1 % num2) != 0:
    print("The two numbers cannot be evenly divided.")
    print(num1 % num2)
else:
    print("The two numbers can be evenly divided.")
    print(num1 % num2)