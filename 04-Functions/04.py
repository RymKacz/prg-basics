text = "You never get a second chance to make a first impression"
i = 0
for char in text:
    if 'e' in char:
        i += 1
print(f'The letter e appears {i} times in the text.')
number = 7
if 7 in range(2, 15):
    print(f'{number} is between 1 and 10')
def f(x,y):
    sum = 0
    i = x
    while i <= y:
        if i < 0:
            if i % 2 == 0:
                sum += 1
        i += 1
    return sum
result = f(-7,8)
print(f'The number of negative even numbers between -7 and 8 is: {result}')
def f(n):
    string =''
    i =0
    while i<n:
        if i % 2 == 0:
            string += "*"
        else:
            string += "/"
        i += 1
    return string
result = f(1)
print(f'The generated string is: {result}')
def f(door):
    minus = 0
    plus = 0
    for char in door:
        if char == '-':
            minus += 1
        elif char == '+':
            plus += 1
    minus2 = minus // 2
    sum = plus - minus2
    if sum >= 3:
        return True
    else:
        return False
result = f("+-++-++-+---")
print(f'{result}')
def f(num1, num2, num3):
    helptable = [num1, num2, num3]
    minimum = min(helptable)
    maximum = max(helptable)
    return maximum - minimum
result = f(7,4,9)
print(f'The difference between the largest and smallest number is: {result}')
def f(name):
    words = name.split()
    acronym = ""

    for w in words:
        acronym += w[0]

    return acronym


# Examples
print(f("Internet of Things"))      # IoT
print(f("For Your Information"))    # FYI
print(f("Python"))                  # P

def f(password):
    # Condition 1: at least 6 characters
    if len(password) < 6:
        return False

    # Condition 2: all characters must be unique
    if len(password) != len(set(password)):
        return False

    return True


# Examples
print(f("ax15"))        # False
print(f("book123"))     # False (two 'o')
print(f("A2water3"))    # True
print(f("qwerty"))      # True
print(f(""))            # False

def f(x,y):
    i =x 
    sum =0
    while i <= y:
        if (i % 6 == 0 and i%4 != 0):
            sum += i
        i += 1
    return sum
result = f(1,20)
print(f'The final value is: {result}')

def factorial(n):
    """Oblicza silnię liczby"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    """Zwraca n-ty element ciągu Fibonacciego"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)