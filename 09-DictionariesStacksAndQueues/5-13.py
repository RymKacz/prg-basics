rpn_string = input("Podaj wyrażenie w notacji odwrotnej polskiej (RPN), elementy oddziel spacją: ")
tokens = rpn_string.split()
stack = []
operators = {'+': lambda x, y: x + y,
             '-': lambda x, y: x - y,
             '*': lambda x, y: x * y,
             '/': lambda x, y: x / y}
for token in tokens:
    if token in operators:
        b = stack.pop()
        a = stack.pop()
        result = operators[token](a, b)
        stack.append(result)
    elif token == '=':
        g = 0
    else:
        stack.append(float(token))
print("Wynik:", stack[0])