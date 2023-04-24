import numpy as np
sardine,tomato = int(input("Sardine : ")),int(input("Tomato : "))
x = np.gcd(sardine,tomato)
print(f"Factory have {sardine} sardine and {tomato} tomatoes\nFactory can make {x} can of canned sardine fishs")



#OUTPUT
"""
Sardine : 300
Tomato : 200
Factory have 300 sardine and 200 tomatoes
Factory can make 100 can of canned sardine fishs
"""