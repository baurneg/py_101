# Print all odd numbers from 1 to 99, inclusive, with each number on a separate line.

# Bonus Question: Can you solve the problem by iterating over just the odd numbers?

for number in range(1, 100, 2):
    print(number)
    
while number < 100:
    print(number % 2 = 1)
    number -= 1
        