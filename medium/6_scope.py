# What is the output of the following code?
# answer = 42
# def mess_with_it(some_number):
# return some_number + 8
# new_answer = mess_with_it(answer)
# print(answer - 8)


answer = 42

def mess_with_it(some_number):
    return some_number + 8

new_answer = mess_with_it(answer)

print(answer - 8)

# will print 34 (42 - 8)
# new_answer will be equal to 50, but it's not printed