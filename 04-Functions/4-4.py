###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    abs_number = abs(number)
    sum_digits = 0
    while abs_number > 0:
        digit = abs_number % 10
        sum_digits += digit
        abs_number //= 10
    return sum_digits

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}.')