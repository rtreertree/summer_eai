dat = 8
if(dat % 2 != 0):
    for i in range(dat):
        layer = list("-"*dat)
        layer[i] = "X"
        layer[(dat-i)-1] = "X"
        print("".join(layer))
else:
    for i in range(dat-1):
        layer = list("-"*dat)
        if(i < dat/2):
            layer[i] = "X"
            layer[(dat-i)-1] = "X"
        else:
            layer[i+1] = "X"
            layer[(dat-i)-2] = "X"

        print("".join(layer))