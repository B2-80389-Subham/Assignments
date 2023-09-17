import pandas as pd

series1 = pd.Series([2, 4, 6, 8, 10])
series2 = pd.Series([1, 3, 5, 7, 9])

addition_result = series1 + series2
subtraction_result = series1 - series2
multiplication_result = series1 * series2
division_result = series1 / series2

results_df = pd.DataFrame({
    'Series1': series1,
    'Series2': series2,
    'Addition': addition_result,
    'Subtraction': subtraction_result,
    'Multiplication': multiplication_result,
    'Division': division_result
})

print(results_df)
