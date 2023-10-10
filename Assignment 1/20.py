import numpy as np

x = np.arange(20, 51)
print(f"Original array: {x}")
print(f"Element-wise remainder of division: {np.remainder(x, 3)}")
