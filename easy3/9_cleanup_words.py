# Given a string that consists of some words and an assortment of 
# non-alphabetic characters, write a function that returns that string 
# with all of the non-alphabetic characters replaced by spaces. If one 
# or more non-alphabetic characters occur in a row, you should only 
# have one space in the result (i.e., the result string should never 
# have consecutive spaces).

# ExampleCopy Code
# print(clean_up("---what's my +*& line?") == " what s my line ")
# # True

def clean_up(my_string):
    my_list = list(my_string)
    for character in my_list:

