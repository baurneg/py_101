# Write a function that takes one integer argument and returns True 
# when the number's absolute value is odd, False otherwise.

def is_odd(number):
    return number % 2 == 0

print(is_odd(8))
print(is_odd(-1))
print(is_odd(0))