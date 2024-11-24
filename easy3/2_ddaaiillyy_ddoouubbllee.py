# Write a function that takes a string argument and 
# returns a new string that contains the value of 
# the original string with all consecutive duplicate 
# characters collapsed into a single character.


# def crunch(my_string):


# print(crunch('ddaaiillyy ddoouubbllee'))

my_string = 'ddaaiillyy ddoouubbllee'
my_list = list(my_string)
index = 0
prev_char = my_list[index]
letter = my_list[index + 1]
new_list = []

while index < len(my_list):
    if letter == prev_char:
        my_list.pop(letter)
    index += 1
    print(new_list)
