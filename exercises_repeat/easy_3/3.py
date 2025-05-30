# Write a function that takes a short line of text and prints it within a box.

# Example 1Copy Code
# print_in_box('To boldly go where no one has gone before.')
# Output for Example 1Copy Code
# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+
# Example 2Copy Code
# print_in_box('')
# Output for Example 2Copy Code
# +--+
# |  |
# |  |
# |  |
# +--+

def inbox(text):
    if len(text) < 75:
        print('+-' + (len(text) * '-') + '-+')
        print('| ' + (len(text) * ' ') + ' |')
        print(f'| {text} |')
        print('| ' + (len(text) * ' ') + ' |')
        print('+-' + (len(text) * '-') + '-+')
inbox('text')