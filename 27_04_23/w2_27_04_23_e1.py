from matplotlib import pyplot as plt
import numpy as np

X_START = 10
X_STOP = 100

y = np.random.rand()
x = np.linspace(X_START, X_STOP, X_STOP - X_START +1)
print(x)

plt.scatter([1, 1], [2 ,3])
plt.show()