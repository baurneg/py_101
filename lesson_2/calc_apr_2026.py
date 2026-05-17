'''Simple Calculator'''

def prompt(message):
    '''prints '==>' before message'''
    print(f"==> {message}")
    
def get_valid_number(prompt_message):
    '''check for valid number'''
    while True:
        prompt(prompt_message)
        valid_number = input()
        try: 
            return float(valid_number)
        except ValueError:
            print("Hmm... that doesn't look like a valid number.")

def get_operation(operation_prompt):
    while True:
        prompt(operation_prompt)
        operation = input()
        if operation in operations:
            return operation
        else:
            print("You must choose 1, 2, 3, or 4.")

def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    while True:
        try:
            return num1/num2
        except ZeroDivisionError:
            print("Can't divide by 0")
            

operations = ['1', '2', '3', '4']    
prompt("Welcome to Calculator!")

valid_number1 = get_valid_number("Please enter your first number: ")
valid_number2 = get_valid_number("Please enter your second number: ")
operation = get_operation('''What operation would you like to perform?
       1) Add 
       2) Subtract 
       3) Multiply 
       4) Divide''')

match operation:
    case "1":
        output = add(valid_number1, valid_number2)
    case "2":
        output = subtract(valid_number1, valid_number2)
    case "3":
        output = multiply(valid_number1, valid_number2)
    case "4":
        output = divide(valid_number1, valid_number2)
        
prompt(f"The result is {output}")


divide(num1):
    """Ask for second number and handle division by zero"""
    while True:
        prompt("Please enter the second number: ")
        num2_str = input()                    # get raw input
        try:
            num2 = float(num2_str)
            return num1 / num2                # if no error, return result
        except ValueError:
            print("Hmm... that doesn't look like a valid number.")
        except ZeroDivisionError:
            print("Can't divide by 0")