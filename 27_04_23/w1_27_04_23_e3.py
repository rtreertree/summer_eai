def calculator(a, b, op):
    match op:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            return a / b
        case _:
            return 0
a, b, op = float(input("Enter a : ")), float(input("Enter b : ")), input("Enter operator (+, -, *, /) : ")
print(f'{a} {op} {b} = {calculator(a,b,op)}')