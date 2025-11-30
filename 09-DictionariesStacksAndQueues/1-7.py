inventory = {
'Laptop': 15,
'Desktop PC': 10,
'Monitor': 25,
'Keyboard': 50,
'Mouse': 60,
'External Hard Drive': 30,
'Printer': 12,
'Router': 20,
'USB Flash Drive': 100,
'Graphics Card': 8
}
sum = 0
for item,quantity in inventory.items():
    print(f'{item}: {quantity}')
for totalquantity in inventory.values():
    sum += totalquantity
        
print(f'Total items in inventory: {sum}')