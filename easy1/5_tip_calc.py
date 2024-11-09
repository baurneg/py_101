bill_amount = float(input('What is the bill? '))
tip_percent = float(input('What is the tip percentage? '))

tip_amount = tip_percent / 100 * bill_amount
total_bill = bill_amount + tip_amount

print(f'The tip is ${tip_amount}')
print(f'The total bill is ${total_bill}')