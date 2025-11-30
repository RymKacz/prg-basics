name = input('Enter your name: ')
if name[-1] == 'a':
    print("Female polish name")
dog_age = 15
age_in_human_years = 0
for year in range(1, dog_age + 1):
    if year <=2:
        age_in_human_years += 10.5
    else:
        age_in_human_years += 4
print(f'Dog age in human years: {age_in_human_years}')
current_product_price = 140
previous_product_price = 200
if current_product_price <= previous_product_price*0.9:
    print("Buy the product!!")
    print(f"Producr price reduced by: {100-(current_product_price/previous_product_price*100)}%")
number_of_products = 5
price = 40
total_cost = 0
for i in range(1, number_of_products +1):
    if i > 2:
        total_cost += price * 0.75
    else:
        total_cost += price
print(f'Total cost: {total_cost}')
ean13 = "5901230094938"
helptable = []
for char in ean13:
    helptable.append(int(char))
if (helptable[0] == 5 and helptable[1] == 9 and helptable[2] == 0):
    print("Product from Poland")
time24 = input("Enter time in 24h format (HH:MM): ")
helptable = time24.split(":")
hours = int(helptable[0])
minutes = int(helptable[1])
if hours >= 12:
    if hours > 12:
        hours -= 12
        print(f'Time in 12h format: {hours}:{minutes} PM')
    else:
        print(f'Time in 12h format: {hours}:{minutes} PM')
elif hours < 12:
    print(f'Time in 12h format: {hours}:{minutes} AM')
elif hours == 24:
    hours = 0
    print(f'Time in 12h format: {hours}:{minutes} AM')
x = 5
y =2
if x > 0 and y >0:
    print("Point is in first quadrant")
elif x < 0 and y >0:
    print("Point is in second quadrant")
elif x < 0 and y <0:
    print("Point is in third quadrant")
elif x > 0 and y <0:
    print("Point is in fourth quadrant")
else:
    print("Point is on axis")
decimal_number= int(input("Enter a decimal number: "))
binary_number = ''
while decimal_number >0:
    remainder = decimal_number % 2
    binary_number += str(remainder)
    decimal_number = decimal_number //2
print("Binary number is: ",binary_number[::-1])

amount = int(input("Enter the amount in PLN: "))

coins_5 = amount // 5
amount %= 5

coins_2 = amount // 2
amount %= 2

coins_1 = amount

print("The amount in coins:")
print("5 PLN coins:", coins_5)
print("2 PLN coins:", coins_2)
print("1 PLN coins:", coins_1)

N = int(input("Enter how many prime numbers to generate: "))

count = 0        # how many primes have been found
number = 2       # first number to test

print("Prime numbers:")

while count < N:
    is_prime = True
    
    # check divisibility from 2 to number - 1
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(number, end=" ")
        count += 1

    number += 1
