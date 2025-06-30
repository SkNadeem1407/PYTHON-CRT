import matplotlib.pyplot as plt
import numpy as np
y=np.array([50, 68, 77, 81])
mylabels=['Apple', 'Mango', 'Guava', 'Kiwi']
myexplode=[0, 0, 0.1, 0]
plt.pie(y, labels=mylabels, startangle=120, explode=myexplode, shadow=True)
plt.legend(title="Different types of fruits:")
plt.show()