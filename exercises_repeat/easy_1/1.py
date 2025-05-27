# Write a function that takes one integer argument and returns True 
# when the number's absolute value is odd, False otherwise.
def is_odd(my_int):
    return abs(my_int % 2) != 0

    
print(is_odd(-9))
print(is_odd(0))
print(is_odd(-6))
print(is_odd(6))


