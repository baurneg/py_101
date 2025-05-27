def valid_input(my_int):
    try: 
        number = int(my_int)
        if number > 0:
            return number
        else: 
            print('Enter a positive number greater than 0')
    except ValueError:
        print('Invalid Input')

my_int = input('Please enter a positive number: ')
operation = input('Please type in \'s\' to calculate the sum and \'p\' to calculate the product: ')
sum = 0
product = 1
operations = ['p', 's']

if operation in operations:
    if operation == 'p':
        for x in range(1, my_int + 1):
            product *= x
    print(product)
    elif operation == 's':
        for x in range (1, my_int + 1):
            sum += x

    print(sum)
else: 
    print('Print valid operation')


print(valid_operation('g'))