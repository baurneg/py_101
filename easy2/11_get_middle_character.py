# Write a function that takes a non-empty string argument 
# and returns the middle character(s) of the string. If 
# the string has an odd length, you should return exactly 
# one character. If the string has an even length, you 
# should return exactly two characters.

# ExamplesCopy Code
# print(center_of('I Love Python!!!') == "Py")    # True
# print(center_of('Launch School') == " ")        # True
# print(center_of('Launchschool') == "hs")        # True
# print(center_of('Launch') == "un")              # True
# print(center_of('Launch School is #1') == "h")  # True
# print(center_of('x') == "x")                    

def center_of(my_string):
    mid_index = my_string[len(my_string) // 2]
    if len(my_string) % 2 != 0:
        return mid_index
    else:
        return mid_index + my_string[int(mid_index) + 1]
    
print(center_of('xyz'))
print(center_of('xyzz'))
