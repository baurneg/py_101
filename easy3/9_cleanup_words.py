# Given a string that consists of some words and an assortment of 
# non-alphabetic characters, write a function that returns that string 
# with all of the non-alphabetic characters replaced by spaces. If one 
# or more non-alphabetic characters occur in a row, you should only 
# have one space in the result (i.e., the result string should never 
# have consecutive spaces).

# ExampleCopy Code
# print(clean_up("---what's my +*& line?") == " what s my line ")
# # True

# def clean_up(my_string):
#     my_list = list(my_string)
#     new_list = []
#     for character in my_list:
#         if 65 < ord(character) < 122:
#             new_list.append(character)
#     print(new_list)

# print(clean_up("---what's my +*& line?"))

my_string = "---what's my +*& line?"
for char in my_string:
    if 65 > ord(char) > 122:
        new_string = my_string.replace(char, ' ', count = 1)
    print(new_string)