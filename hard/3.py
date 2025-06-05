# Given the following similar sets of code, 
# what will each code snippet print?

# def mess_with_vars(one, two, three):
#     one = two
#     two = three
#     three = one

# one = ["one"]
# two = ["two"]
# three = ["three"]

# mess_with_vars(one, two, three) # ('one', 'two', 'three')
# 'two',
# 'three'
# 'one'


# print(f"one is: {one}")
# print(f"two is: {two}")
# print(f"three is: {three}")

def mess_with_vars(one, two, three):
    one = ["two"]
    two = ["three"]
    three = ["one"]

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")