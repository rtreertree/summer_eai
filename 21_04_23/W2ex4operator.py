import numpy as np

r = float(input("Radius (m): "))
h = float(input("Height (m) : "))
print(f'Volume = {(1/3)*np.pi*np.power(r, 2)*h} m^3')

#OUTPUT
"""
Radius (m): 10
Height (m) : 45
Volume = 4712.38898038469 m^3
"""