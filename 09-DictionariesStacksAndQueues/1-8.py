price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}
for item,price in price_list.items():
    print(f'{item}: ${price}')
sum = 0
for total_price in price_list.values():
    sum += total_price
print(f'Total price of all items: ${sum:.2f}')
for item,discounted_price in price_list.items():
    print(f'{item} after 10% discount: ${discounted_price * 0.9:.2f}')
discounted_sum = 0
for discounted_price in price_list.values():
    discounted_sum += discounted_price * 0.9
print(f'Total price after discounts: ${discounted_sum:.2f}')