# Write a function that takes two arguments, a string and 
# a positive integer, then prints the string as many times as the integer indicates.

def repeat(my_string, number):
    for word in range(number):
        print(my_string)

repeat('Hello', 3)