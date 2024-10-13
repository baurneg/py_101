# Even Numbers
# Print all even numbers from 1 to 99, inclusive, with each number on a separate line.

# Bonus Question: Can you solve the problem by iterating over just the even numbers?

print('Printing even numbers in the range of given numbers')
n1 = int(input('Please enter a starting number: '))
n2 = int(input('Please enter an ending number: '))

for number in range(n1, n2 + 2, 2):
    if number % 2 == 0:
        print(number)
