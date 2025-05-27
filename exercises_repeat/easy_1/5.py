# Create a simple tip calculator. The program should prompt for a bill amount and a tip rate. 
# The program must compute the tip, then print both the tip and the total amount of the bill. 
# You can ignore input validation and assume that the user will enter valid numbers.

# ExampleCopy Code
# What is the bill? 200
# What is the tip percentage? 20

def valid_float(my_input):
    while True:
        try:
            return float(input(my_input))
        except ValueError:
            print('Invalid input!')

bill = valid_float('What\'s the bill amount?')
tip_percent = valid_float('What\'s the tip percentage? ')

tip_amount = bill * (tip_percent/100)
total = bill + tip_amount

print(f'The tip is ${tip_amount:.2f}')
print(f'The total is ${total:.2f}')