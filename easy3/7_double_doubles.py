# A double number is an even-length number whose left-side digits are exactly 
# the same as its right-side digits. For example, 44, 3333, 103103, and 7676 
# are all double numbers, whereas 444, 334433, and 107 are not.

# Write a function that returns the number provided as an argument multiplied 
# by two, unless the argument is a double number. If the argument is a double 
# number, return the double number as-is.

# ExamplesCopy Code
# print(twice(37) == 74)                  # True
# print(twice(44) == 44)                  # True
# print(twice(334433) == 668866)          # True
# print(twice(444) == 888)                # True
# print(twice(107) == 214)                # True
# print(twice(103103) == 103103)          # True
# print(twice(3333) == 3333)              # True
# print(twice(7676) == 7676)              # True

def twice(number):
    number_string = str(number)    
    half_string = int(len(number_string) / 2)    
    if len(number_string) % 2 != 0:
        return number * 2
    if (number_string[0:half_string]) == (number_string[half_string:len(number_string)]):
        return number
    else:
        return number * 2

print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True