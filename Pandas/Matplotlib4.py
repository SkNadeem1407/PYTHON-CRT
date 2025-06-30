import matplotlib.pyplot as plt
import numpy as np
x=np.array([5,7,8,2,3])
y=np.array([6,9,11,16,23])
colors=np.array([10,20,30,40,50])
plt.scatter(x,y, c=colors ,cmap='viridis')
plt.show()