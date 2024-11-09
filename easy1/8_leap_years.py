# Write a function that takes any year greater than 0 as input and returns True 
# if the year is a leap year, or False if it is not.

# For simplicity, this exercise assumes that the Gregorian calendar has been 
# in continuous use since the year 1. We'll address that assumption in the next 
# exercise that follows this one.

# To determine whether a given year is a leap year, use the rules of the Gregorian 
# calendar:

# If the year is divisible by 400, it is a leap year.
# If the year is divisible by 100 but not by 400, it is not a leap year.
# If the year is divisible by 4 but not by 100, it is a leap year.
# All other years are not leap years.
# ExamplesCopy Code
# # These examples should all print True


def is_leap_year(year):
    return ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)

print(is_leap_year(1))
print(is_leap_year(2))
print(is_leap_year(3))
print(is_leap_year(4))
print(is_leap_year(1000))
print(is_leap_year(1100))
print(is_leap_year(1200))
print(is_leap_year(1300))
print(is_leap_year(1751))
print(is_leap_year(1752))
print(is_leap_year(1753))
print(is_leap_year(1800))
print(is_leap_year(1900))
print(is_leap_year(2000))
print(is_leap_year(2023))
print(is_leap_year(2024))
print(is_leap_year(2025))