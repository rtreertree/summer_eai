import numpy as np
w = float(input("Weight : "))
h = float(input("Height : "))

print(f"Mosteller's Body suface area : {float(np.sqrt(w*h))/60}")
print(f"Haycock's Body suface area : {0.024265*np.power(w, 0.5378)*np.power(h, 0.3964)}")
print(f"Boyd's Body suface area : {(0.0333*np.power(w, 0.6157-0.0188*np.log10(w)))*np.power(h, 0.3)}")

#OUTPUT
"""
Weight : 56
Height : 173
Mosteller's Body suface area : 1.6404606399152375
Haycock's Body suface area : 1.6304868174022364
Boyd's Body suface area : 1.632155747802396
"""