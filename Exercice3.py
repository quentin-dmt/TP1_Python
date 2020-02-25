import numpy as np
V1 = np.ones(4)*2
V2 = np.insert(V1,2,5)
print(V2)
V2 = V2.reshape(1,5)
print(V2)
A = np.concatenate([V2]*6, axis = 0)
print(A)