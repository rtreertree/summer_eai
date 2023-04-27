import numpy as np
list_a, list_b = input('Enter list : ').split(" "), []
for i in list_a:
    list_b.append(int(i))
print(f"Median is : {np.median(list_b)}")