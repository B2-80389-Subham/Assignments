import numpy as np
arr_x = [1, 2, 3]
arr = np.arange(2, 9)
print(f"array : {arr}")
print(f"reversed array :{np.flip(arr)}")
print(f"reversed array :{arr[::-1]}")  # method2
print(f"python list :   {arr_x}")
print(f"reversed list : {arr_x[::-1]}")
