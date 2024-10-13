# Print all odd numbers from 1 to 99, inclusive, with each number on a separate line.

# Bonus Question: Can you solve the problem by iterating over just the odd numbers?
print('Printing odd numbers in the range of given numbers')
n1 = int(input('Please enter a starting number: '))
n2 = int(input('Please enter an ending number: '))

for number in range(n1, n2, 2):
    print(number)
    
# while number < 100:
#     print(number % 2 = 1)
#     number -= 1