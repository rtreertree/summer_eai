import numpy as np

class class_21_04():
    def A14():
        text = input('Enter something : ')
        print(f'Your data : {text}, data type is : {type(text)}')

    def A17():
        name = input('Enter your name : ')
        print(f'Your name is {name} ; data type is : {type(name)}')

    def A21():
        a = float(input('x : '))
        b = float(input('y : '))
        print(f'{a} + {b} = {a + b} ; data type is : {a + b}')
        print(f'{a} - {b} = {a - b} ; data type is : {a - b}')
        print(f'{a} * {b} = {a * b} ; data type is : {a * b}')
        print(f'{a} / {b} = {a / b} ; data type is : {a / b}')

    def A22():
        float_var = float(input('variable 1 : '))
        int_var = int(input('variable 2 : '))
        print(f'variable 1 : {float_var} ; datatype : {type(float_var)}')
        print(f'variable 2 : {int_var} ; datatype : {type(int_var)}')
        print(f'{float_var} - {int_var} = {float_var-int_var} ; datatype : {type(float_var-int_var)}')
        print(f'{float_var} + {int_var} = {float_var+int_var} ; datatype : {type(float_var+int_var)}')


    def A23_1():
        f = float(input('F : '))
        s = float(input('S : '))
        print(f'W = FS; W = {f}x{s}; W = {f*s}')

    def A23_2():
        w = float(input('W : '))
        t = float(input('T : '))
        print(f'P = W/T; P = {w}x{t}; W = {w*t}')

    def A24():
        name = input('name : ')
        surname = input('surname : ')
        age = int(input('age : '))
        age_sister = int(input('sister_age : '))
        print(f'name = {name}; datatype = {type(name)}')
        print(f'surname = {surname}; datatype = {type(surname)}')
        print(f'age = {age}; datatype = {type(age)}')
        print(f'sister_age = {age_sister}; datatype = {type(age_sister)}')
        print(f'diff = {np.abs(age-age_sister)}')


    def A25():
        r = float(input("Radius (m): "))
        h = float(input("Height (m) : "))
        print(f'Volume = {(1/3)*np.pi*np.power(r, 2)*h} m^3')

    def A26():
        x = float(input(" x : "))
        y = float(input(" y : "))
        print(f"Result = {x > y}; data type {type(x > y)}")
