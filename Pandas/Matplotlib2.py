import numpy as np
import matplotlib.pyplot as plt
x=np.array([25,48,30,78,45,12])
y=np.array([22,18,13,10,50,14])

plt.title("Sports Watch Data", loc= 'right')
plt.xlabel=("Average Pulse")
plt.ylabel=("Calorie Burnage")
plt.plot(x ,y)
plt.grid(axis= 'x',color='black',linestyle='--',linewidth=5)
plt.show()