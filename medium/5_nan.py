# What do you think the following code will output?

# nan_value = float("nan")
# print(nan_value == float("nan" ))
# Bonus Question
# How can you reliably test if a value is nan ?


nan_value = float("nan")
print(nan_value == float("nan"))

# returns false
# need to import math module
# use math.isnan() function to evaluate 'nan', Python does not allow for raw evaluation
