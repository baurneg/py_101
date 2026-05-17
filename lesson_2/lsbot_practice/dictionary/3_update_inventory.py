# 3. Update Inventory

# •   ​Difficulty​: Advanced
# •   ​Description​: Write a function update_inventory that takes two dictionaries 
# as arguments: current_stock and new_shipment. The function should update 
# current_stock by adding the quantities from new_shipment. If an item from 
# new_shipment is not in current_stock, it should be added. This function should 
# modify the current_stock dictionary in place and not return anything.

def update_inventory(stock, shipment):
    for k, v in shipment.items():
        if k in shipment.keys():
            stock[k] += shipment[v]
            print(stock)
            print(shipment)


#     ​Test Cases:

stock = {'apples': 10, 'bananas': 20}
shipment = {'bananas': 5, 'oranges': 15}
update_inventory(stock, shipment)
print(stock)
# Expected output: {'apples': 10, 'bananas': 25, 'oranges': 15}

# stock2 = {'pens': 100, 'pencils': 150}
# shipment2 = {'pencils': 50, 'erasers': 75}
# update_inventory(stock2, shipment2)
# print(stock2)
# # Expected output: {'pens': 100, 'pencils': 200, 'erasers': 75}