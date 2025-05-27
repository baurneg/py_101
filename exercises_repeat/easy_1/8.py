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
def valid_year():
    while True:
        try:
            year = int(input("Please enter a year: "))
            if year <= 0:
                print('Please enter a valid number! ')
                continue
            return year
        except ValueError:
            print('Invalid input! Please enter a year!')
# print(valid_year('1100'))
# print(valid_year('-1100'))
# print(valid_year('abv'))


# def leap_year(year):
#     while valid_year(year) > 0:
#         if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#             return True
#         else:
#             return False

# # year = int(input('Enter the year: '))
# print(leap_year('1990'))