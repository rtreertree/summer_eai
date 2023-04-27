text = input("User input : ")

data_x, data_y = [], []

current_char = ""
counts = 0
for char in text:
    if(char == current_char):
        counts += 1
    else:
        if(counts != 0):
            data_x.append(current_char)
            data_y.append(counts)
        current_char = char
        counts = 1

data_x.append(current_char)
data_y.append(counts)

print(data_x, data_y)