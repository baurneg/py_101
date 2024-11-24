# Build a program that displays when the user will retire 
# and how many years she has to work till retirement.

# ExampleCopy Code
# What is your age? 30
# At what age would you like to retire? 70

# It's 2024. You will retire in 2064.
# You have only 40 years of work to go!

current_age = input(int('What is your age?'))
retirement_age = input(int('At what age would you like to retire?'))

print(f'It\'s 2024. You will retire in {2024 + {retirement_age - current_age}}')