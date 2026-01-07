'''Simple Calculator'''

def prompt(message):
    '''prints '==>' before message'''
    print(f"==> {message}")

def invalid_number(number_str):
    '''check for valid number'''
    try:
        int(number_str)
    except ValueError:
        return True
    except ZeroDivisionError:
        return True

    return False

prompt('Welcome to Calculator!')

prompt("What's the first number?")
number1 = input()

while invalid_number(number1):   
    number1 = prompt(input("Hmm... that doesn't look like a valid number."))
    number2 = input(prompt("What's the second number?"))

while invalid_number(number2):
    prompt("Hmm... that doesn't look like a valid number.")
    number2 = input()

prompt('''What operation would you like to perform?
       1) Add 2) Subtract 3) Multiply 4) Divide''')
operation = input()

while operation not in ["1", "2", "3", "4"]:
    prompt("You must choose 1, 2, 3, or 4")
    operation = input()

match operation:
    case "1":
        output = int(number1) + int(number2)
    case "2":
        output = int(number1) - int(number2)
    case "3":
        output = int(number1) * int(number2)
    case "4":
        if number2 != 0:
            output = int(number1) / int(number2)
        else:
            print('not a valid number')
prompt(f"The result is {output}")
