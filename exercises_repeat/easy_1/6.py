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

def valid_float(my_input):
    while True:
        try:
            num = float(input(my_input))
            if num > 0:
                return num
            else: 
                print('This doesn\'t look like a number greater than 0. Please try again!')        
        except ValueError:
            print('Invalid input! Please try again!')

def valid_operation(operation):
    operations = ['s', 'p']
    while operation not in operations:
        print("Invalid input! Please enter 's' or 'p':")
        operation = input().lower()  # Prompt for new input and convert to lowercase
    return operation
        
def compute_sum(number):
    sum = 0
    for number in range(1, int(number) + 1):
        sum += number
    return sum
def compute_product(number):
    product = 1
    for number in range(1, int(number) + 1):
        product *= number
    return product

my_int = valid_float('Please enter a number greater than 0: ')
operation = valid_operation(input("Please enter 's' to calculate the sum of intergers, 'p' to calculate the product: "))
if operation == 's':
    print(f'The sum of all the consecutive numbers is {compute_sum(my_int)}')
elif operation == 'p':
    print(f'The product of all the consecutive numbers is {compute_product(my_int)}')