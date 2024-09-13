'''Mortgage Calculator'''
import os

def prompt(message):
    '''message separator'''
    print(f'==> {message}')

def invalid_number(number_str):
    '''check for valid number'''
    try:
        float(number_str) # checks if input can be converted to float
        if float(number_str) < 0:
            return True # checks if input is less than 0
    except ValueError:
        return True
    return False

def valid_loop(repeat):
    '''Prompts until valid input ('y' or 'n') is provided. 
    Returns True for 'n' (no), and False for 'y' (yes).'''
    while repeat not in ['y', 'n']:
        repeat = input("Please enter 'y' for yes or 'n' for no: ").lower()
    return repeat == 'n'


prompt('Welcome to your mortgage calculator!')
while True:
    prompt('Please enter your loan amount: ')
    loan_amount = input()
    while invalid_number(loan_amount):
        prompt("Hmm... that doesn't look like a valid number. Please enter a valid number")
        loan_amount = input()

    prompt('Please enter your APR: ')
    apr_value = input()
    while invalid_number(apr_value):
        prompt("Hmm... that doesn't look like a valid number. Please enter a valid number")
        apr_value = input()
    if float(apr_value) < 1:
        print('''"Are you sure your APR is based on an annual percentage out of 100%?
              Enter 'y' to confirm or 'n' to enter a new APR value"''')
        apr_value_confirm = input()
        if valid_loop(apr_value_confirm):
            apr_value = input("Please enter a new APR value: ")

    prompt('Please enter the loan duration in years: ')
    loan_duration = input()
    while invalid_number(loan_duration):
        prompt("Hmm... that doesn't look like a valid number. Please enter a valid number")
        loan_duration = input()

    loan_duration_months = float(loan_duration) * 12
    monthly_rate = (float(apr_value)/12)/100

    if monthly_rate == 0:
        monthly_payment = float(loan_amount)/float(loan_duration_months)
    else:
        monthly_payment = float(loan_amount) * (monthly_rate / (1 - (1 + monthly_rate) ** (-(float(loan_duration_months)))))
    os.system('clear')
    prompt(f'Your monthly payment equals to {round(monthly_payment, 2)} for a loan of ${loan_amount} at {apr_value}% APR for {loan_duration} years (or {loan_duration_months} months)')
    prompt('Would you like to do another calculation? Enter "y" for yes, "n" for no')
    another_calculation = input()
    os.system('clear')

    if valid_loop(another_calculation):
        os.system('clear')
        prompt("Thanks for using my mortgage calculator!")
        break
