def gen_line(line, char):
    textlayer = ""
    num = ((1 if char == ' ' else 2)*line)-1
    for i in range(num):
        textlayer = textlayer + char
    return textlayer

def print_pyramid(linecount):
    linecount +=1
    layer, space = [], []
    new_layer = []
    for i in range(1, linecount):
        layer.append(gen_line(i,'*'))
        space.append(gen_line(i,' '))
    for i, l in enumerate(layer):
        if i+2 == linecount or i == 0:
            new_layer.append(l)
        else:
            lay = list(layer[i])
            for i in range(1, len(lay)):
                if i == len(lay)-1:
                    pass
                else:
                    lay[i] = " "
            new_layer.append("".join(lay))
    space.reverse()
    for i in range(linecount - 1):
        print(space[i]+new_layer[i])


count = int(input("Enter layers count : "))
print_pyramid(count)