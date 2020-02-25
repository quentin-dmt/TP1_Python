import matplotlib.pyplot as plt
import numpy as np
np.random.seed(1997)
norm = np.random.normal(6, 3, 10000)
plt.hist(norm,bins='sturges',density=True)  #sturges
x = np.linspace(-6,16,220)
y = (1./(np.sqrt(2.*np.pi*9.)))*np.exp(-(1./2.)*((x-6.)/3.)**2.)
plt.plot(x,y,color='black')
plt.show()