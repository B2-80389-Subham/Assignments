import pandas as pd

input_data = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
original_series = pd.Series(input_data)
print("Original input_data Series:")
print(original_series)

new_index_order = ['B', 'A', 'C', 'D', 'E']
changed_order_series = original_series.reindex(new_index_order)
print("\ninput_data Series after changing the order of index:")
print(changed_order_series)
