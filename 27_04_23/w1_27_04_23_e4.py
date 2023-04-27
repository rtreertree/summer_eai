import numpy as np
def find_min_max(list_a):
    return np.min(list_a), np.max(list_a)

print(find_min_max([1, 2 ,3, 4, 5, 100]))

#OUTPUT
"""
(1, 100) 
"""