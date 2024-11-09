# Write a function that takes two strings as arguments, determines the length of 
# the two strings, and then returns the result of concatenating the shorter string, 
# the longer string, and the shorter string once again. You may assume that the strings 
# are of different lengths.

# ExamplesCopy Code
# # These examples should all print True
# print(short_long_short('abc', 'defgh') == "abcdefghabc")
# print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
# print(short_long_short('', 'xyz') == "xyz")

def short_long_short(str1, str2):
    if len(str1) < len(str2):
        return (str1 + str2 + str1)
    elif len(str2) < len(str1):
        return (str2 + str1 + str2)
    else:
        print('The strings are of equal length')

print(short_long_short('abc', 'defgh'))
print(short_long_short('abcde', 'fgh'))
print(short_long_short('', 'xyz'))
print(short_long_short('abc', 'xyz'))