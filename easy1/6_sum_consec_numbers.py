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

def sum_numbers(number):
    sum = 0
    for number in range(1, int(n) + 1):
        sum += number
    return sum

def product_numbers(number):
    product = 1
    for number in range(1, int(number) + 1):
        product *= number
    return product
def invalid_number(number):
    try:
        number = int(number)
        return number < 0
    except ValueError:
        return True

OPTIONS = ['s', 'p']
print('Please enter an integer greater than 0: ')
number = input()
while invalid_number(number):
    print("Input is not a valid number. Please enter a positive number: ")
    number = input()
print('Enter "s" to compute the sum, or "p" to compute the product: ')
operation = input()
if operation not in OPTIONS:
    print('Please enter either "s" or "p":')
    operation = input()
else:
    if operation == 'p':
        print(f'The product of the integers between 1 and {number} is {product_numbers(number)}.')
    else:
        print(f'The sum of the integers between 1 and {number} is {sum_numbers(number)}.')
