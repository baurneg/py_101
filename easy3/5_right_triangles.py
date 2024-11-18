# Write a function that takes a positive integer, n, as an argument 
# and prints a right triangle whose sides each have n stars. 
# The hypotenuse of the triangle (the diagonal side in the images 
# below) should have one end at the lower-left of the triangle, 
# and the other end at the upper-right.

# Example 1Copy Code
# triangle(5)
# Output for Example 1Copy Code
#     *
#    **
#   ***
#  ****
# *****
# Example 2Copy Code
# triangle(9)
# Output for Example 2Copy Code
#         *
#        **
#       ***
#      ****
#     *****
#    ******
#   *******
#  ********
# *********

for symbol in range(5):
    print(symbol * '*')