import numpy as np
A = np.array([[5, 2.6, 5, 9], [4, 3.6, 9, 10], [5.5, 4, 6, 7]])
print(A)

print(np.mean(A, axis = 0))
print(np.mean(A, axis = 1))