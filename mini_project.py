# Student Result Analyzer
import numpy as np
marks = np.array([78,85,92,67,88,95,72])
print("Average:",np.mean(marks))
print("highest:", np.max(marks))
print("lowest:",np.min(marks))
print("Student above 80:",marks[marks>80])

# Bonus Challenge (Without loops)
arr = np.array([10, 20, 30, 40, 50])
new_arr = arr *2
print(new_arr)
print("Average:", np.mean(new_arr))
