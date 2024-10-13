
# def check(number1, number2):
#     if number1 * number2 > 1000:
#         print(f'The result is {number1 + number2}')
#     else:
#         print(f'The result is {number1 * number2}')
    
# number1 = float(input(f'Enter number 1: '))
# number2 = float(input(f'Enter number 2: '))
# check(number1, number2)

# number = int(input('Enter a number: '))
# print(f'Printing current and previous number sum in a range({number})')
# previous_number = 0
# for number in range(number):
#     print(f'Current Number {number} Previous Number  {previous_number}  Sum:  {number + previous_number}')
#     number += 1
#     previous_number = number - 1



# Printing current and previous number sum in a range(10)
# Current Number 0 Previous Number  0  Sum:  0
# Current Number 1 Previous Number  0  Sum:  1
# Current Number 2 Previous Number  1  Sum:  3
# Current Number 3 Previous Number  2  Sum:  5
# Current Number 4 Previous Number  3  Sum:  7
# Current Number 5 Previous Number  4  Sum:  9
# Current Number 6 Previous Number  5  Sum:  11
# Current Number 7 Previous Number  6  Sum:  13
# Current Number 8 Previous Number  7  Sum:  15
# Current Number 9 Previous Number  8  Sum:  17

# Write a Python code to accept a string from the user and display characters present at an even index number.

# For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.

# Expected Output:

# Orginal String is  PYnative
# Printing only even index chars
# P
# n
# t
# v

# Exercise 4: Remove first n characters from a string
# Write a Python code to remove characters from a string from 0 to n and return a new string.

# For Example:

# remove_chars("PYnative", 4) so output must be tive. Here, you need to remove the first four characters from a string.
# remove_chars("PYnative", 2) so output must be native. Here, you need to remove the first two characters from a string.
# Note: n must be less than the length of the string.

# numbers_x = [10, 20, 30, 40, 10]
# numbers_y = [75, 65, 35, 75, 30, 75]
# # Expected Output:

# # Given list: [10, 20, 30, 40, 10]
# # result is True

# # numbers_y = [75, 65, 35, 75, 30]
# # result is False

# def first_last_identical(my_list_1):
#     if my_list_1[0] == my_list_1[-1]:
#         return True
#     else:
#         return False
# print(first_last_identical(numbers_x))
# print(first_last_identical(numbers_y))

my_var = "Hello"

def my_func():
    my_var = my_var + " world"
    # UnboundLocalError: local variable 'my_var' referenced before assignment
    return my_var

(my_func())
print(my_var)