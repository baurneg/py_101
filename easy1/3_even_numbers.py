# Even Numbers
# Print all even numbers from 1 to 99, inclusive, with each number on a separate line.

# Bonus Question: Can you solve the problem by iterating over just the even numbers?

for number in range(1, 99):
    if number % 2 == 0:
        print(number)
