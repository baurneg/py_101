# Write a function that determines and returns the UTF-16 string value of 
# a string passed in as an argument. The UTF-16 string value is the sum 
# of the UTF-16 values of every character in the string. (You may use ord 
# to determine the UTF-16 value of a character.)

# Examples

utf_16_value = ''
def utf16_value(my_string):
    sum = 0

    for letter in my_string:
        sum += ord(letter)
    return sum

print(utf16_value('Four score'))
print(utf16_value('Launch School'))
print(utf16_value('a'))
print(utf16_value(''))

# # The next three lines demonstrate that the code
# # works with non-ASCII characters from the UTF-16
# # character set.
OMEGA = "\u03A9"              # UTF-16 character 'Ω' (omega)
print(utf16_value(OMEGA) == 937)
print(utf16_value(OMEGA + OMEGA + OMEGA))