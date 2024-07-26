# Write a function that takes one integer argument and returns True 
# when the number's absolute value is odd, False otherwise.

def is_odd(integer):
    return abs(integer) % 2 != 0
    
    
    
    
print(is_odd(-3))
print(is_odd(4))