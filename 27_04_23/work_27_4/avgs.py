import numpy as np
list_a, list_b = input('Enter list : ').split(" "), []
for i in list_a:
    list_b.append(int(i))
print(f"Average is : {np.average(list_b)}")