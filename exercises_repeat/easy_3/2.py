# Write a function that takes a string argument and 
# returns a new string that contains the value of 
# the original string with all consecutive duplicate 
# characters collapsed into a single character.


def crunch(my_string):
    my_list = list(my_string)
    index = 0
    new_list = []
    while index + 1 < len(my_string):
        prev_char = my_list[index]
        char = my_list[index + 1]
        if char == prev_char:
            new_list.append(char)
            print(new_list)
        index += 1
    print(my_list)

print(crunch('ddaaiillyy  ddoouubbllee'))

