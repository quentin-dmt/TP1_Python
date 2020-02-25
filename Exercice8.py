import numpy as np
import matplotlib.pyplot as plt
n = np.sum(np.random.binomial(1., 1./3., 100))
loi_a = np.concatenate([np.random.normal(0,1,n).reshape(n,1),np.random.normal(0,1,n).reshape(n,1)], axis = 1)
loi_b = np.concatenate([np.random.normal(1,np.sqrt(0.25),100-n).reshape(100-n,1),np.random.normal(1,np.sqrt(0.25),100-n).reshape(100-n,1)], axis = 1)
print(loi_a)
print(loi_a.shape)
print(loi_b.shape)

x = np.concatenate([loi_a[:,0],loi_b[:,0]])
print(len(x))
y = np.concatenate([loi_a[:,1],loi_b[:,1]])
print(len(y))
plt.scatter(x,y,color="blue",alpha=0.6)
plt.show()