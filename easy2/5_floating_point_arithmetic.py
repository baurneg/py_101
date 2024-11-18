# Floating Point Arithmetic
# Write a program that prompts the user for two positive 
# numbers (floating-point), then prints the results of the 
# following operations on those two numbers: addition, subtraction, 
# product, quotient, floor quotient, remainder, and power. Do not 
# worry about validating the input.

# ExamplesCopy Code
# ==> Enter the first number:
# 3.141529
# ==> Enter the second number:
# 2.718282
# ==> 3.141529 + 2.718282 = 5.859811
# ==> 3.141529 - 2.718282 = 0.42324699999999993
# ==> 3.141529 * 2.718282 = 8.539561733178
# ==> 3.141529 / 2.718282 = 1.1557038600115808
# ==> 3.141529 // 2.718282 = 1.0
# ==> 3.141529 % 2.718282 = 0.42324699999999993
# ==> 3.141529 ** 2.718282 = 22.45792517468373

def prompt(message):
    return (f'==> {message} ')
number1 = (input(prompt('Enter the first number:\n')))
number2 = (input(prompt('Enter the second number:\n')))
print(prompt(f'{float(number1)} + {float(number2)} = {float(number1) + float(number2)} '))
print(prompt(f'{float(number1)} - {float(number2)} = {float(number1) - float(number2)} '))
print(prompt(f'{float(number1)} * {float(number2)} = {float(number1) * float(number2)} '))
print(prompt(f'{float(number1)} / {float(number2)} = {float(number1) / float(number2)} '))
print(prompt(f'{float(number1)} // {float(number2)} = {float(number1) // float(number2)} '))
print(prompt(f'{float(number1)} % {float(number2)} = {float(number1) % float(number2)} '))
print(prompt(f'{float(number1)} ** {float(number2)} = {float(number1) ** float(number2)} '))