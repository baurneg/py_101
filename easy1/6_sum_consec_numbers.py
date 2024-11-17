# Write a program that asks the user to enter an integer greater than 0,
# then asks whether the user wants to determine the sum or the product of
# all numbers between 1 and the entered integer, inclusive.

# Example 1Copy Code
# Please enter an integer greater than 0: 5
# Enter "s" to compute the sum, or "p" to compute the product. s

# The sum of the integers between 1 and 5 is 15.
# Example 2Copy Code
# Please enter an integer greater than 0: 6
# c p

# The product of the integers between 1 and 6 is 720.

'''Sum of consecutive numbers'''
OPTIONS = ['s', 'p']
def invalid_number(number):
    try:
        number = int(number)
        if number <= 0: 
          return True
    except ValueError:
        return True
def sum(number):
    sum_numbers = 0
    for item in range(1, number + 1):
        sum_numbers += item
    return (sum_numbers)
def product(number):
    product_number = 1
    for item in range(1, number + 1):
        product_number *= item
    return (product_number)

number_value = input('Please enter an integer greater than 0: ')
while invalid_number(number_value):
    print('Please enter a valid number: ')
    number_value = input()
print('Enter "s" to compute the sum, or "p" to compute the product: ')
operation = input()
product_value = product(int(number_value))
sum_value = sum(int(number_value))
while operation not in OPTIONS:
    print('Please enter either "s" or "p":')
    operation = input()
if operation == 'p':
    print(f'The product of the integers between 1 and {number_value} is {product_value}.')
else:
    print(f'The sum of the integers between 1 and {number_value} is {sum_value}.')
