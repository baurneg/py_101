# Write a function that takes a string argument and 
# returns a new string that contains the value of 
# the original string with all consecutive duplicate 
# characters collapsed into a single character.


# def crunch(my_string):


# print(crunch('ddaaiillyy ddoouubbllee'))

my_string = 'ddaaiillyy ddoouubbllee'
prev_char = ''

for letter in range(len(my_string)):
