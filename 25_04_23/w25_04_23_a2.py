X = []
for i in range(9):
    text = ""
    for n in range(i+1):
        text += "x"
    X.append(text)
X.reverse()
for layer in X:
    print(layer)