def prompt(message):
    '''message separator'''
    print(f'==> {message}')

def invalid_number(number_str):
    '''check for valid number'''
    try:
        float(number_str)
        if float(number_str) < 0:
            return True
    except ValueError:
        return True
    return False

def valid_loop(yes_no):
    '''Prompts until valid input ('y' or 'n') is provided. Returns True for 'y' (yes), and False for 'n' (no).'''
    while yes_no not in ['y', 'n']:
        yes_no = input("Please enter 'y' for yes or 'n' for no: ").lower()
    return yes_no == 'n'


prompt('Welcome to your mortgage calculator!')
while True:

    prompt('Please enter your loan amount: ')
    loan_amount = input()
    while invalid_number(loan_amount):
        prompt("Hmm... that doesn't look like a valid number. Please enter a valid number")

    prompt('Please enter your APR: ')
    apr_value = input()
    while invalid_number(apr_value):
        prompt("Hmm... that doesn't look like a valid number. Please enter a valid number")
        apr_value = input()


    prompt('Please enter the loan duration in years: ')
    loan_duration = input()
    while invalid_number(loan_duration):
        prompt("Hmm... that doesn't look like a valid number. Please enter a valid number")
        break
    loan_duration_months = float(loan_duration) * 12


    monthly_rate = (float(apr_value)/12)/100

    if monthly_rate == 0:
        monthly_payment = float(loan_amount)/float(loan_duration_months)
    else:
        monthly_payment = float(loan_amount) * (monthly_rate / (1 - (1 + monthly_rate) ** (-(float(loan_duration_months)))))

    prompt(f'Your monthly payment equals {round(monthly_payment, 2)}')
    prompt('Would you like to do another calculation? Press "y" for yes, "n" for no')
    another_calculation = input()
    if valid_loop(another_calculation):
        break