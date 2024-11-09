VALID_CHOICES = ['rock', 'paper', 'scissors']
choices = .join(

def prompt(message):
    print(f'==> {message}')

prompt(f'Choose one: rock, paper, scissors')
choice = input()

while choice not in VALID_CHOICES:
    prompt('Not a valid choice. Please enter `rock`, `paper` or `scissors`')
    choice = input()

