number, dashs= [], []
for i in range(9):
    text = ""
    for n in range(1, i+2): text += str(n)
    number.append(text)
    dashs.append("-"*i)
dashs.reverse()
for text, dash in zip(number, dashs):
    print(dash + text)

#OUTPUT
"""
--------1
-------12
------123
-----1234
----12345
---123456
--1234567
-12345678
123456789
"""