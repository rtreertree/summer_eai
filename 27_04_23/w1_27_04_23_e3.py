def calculator(a,b,op):
    return eval(f"{a}{op}{b}")
a,b,op = input("A :"), input("B :"), input("Op :")
print(f"Anwser is {calculator(a,b,op)}")

#OUTPUT
"""
A :100
B :50
Op :/
Anwser is 2.0
"""