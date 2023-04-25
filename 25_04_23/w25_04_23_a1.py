number = []
dashs = []
for i in range(9):
    text = ""
    dash = ""
    for n in range(1, i+2): text += str(n)
    for n in range(1, i+1): dash += "-"
    number.append(text)
    dashs.append(dash)

dashs.reverse()
print(dashs)
for text, dash in zip(number, dashs):
    print(dash + text)