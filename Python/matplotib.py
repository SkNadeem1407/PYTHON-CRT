'''import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt
A=np.array([1,2,3,4])
B=np.array([2,3,4,5])
plt.plot(A,B,marker='o',color='g')
plt.show()'''
import matplotlib.pyplot as plt
import numpy as np

'''import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3,8,1,10])
plt.plot(ypoints, 'o:r',ms=25)
plt.show()'''

'''import numpy as np
import matplotlib.pyplot as plt
x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])
plt.plot(x ,y)
plt.title("Sports Watch Data", loc = 'right')
plt.xlabel("Average Pulse")
plt.ylabel("calorie Burnage")
plt.show()'''

'''import numpy as np
import matplotlib.pyplot as plt
x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,240,310,320,330])

plt.title("Sports Watch Data", loc = 'right')
plt.xlabel("Average Pulse")
plt.ylabel("calorie Burnage")
plt.plot(x ,y)
plt.grid(axis= 'x',color='yellow',linestyle= '--',linewidth=5)
plt.show()
'''


'''import numpy as np
import matplotlib.pyplot as plt
#plot1:
x=np.array([0,1,2,3])
y=np.array([3,8,1,10])
plt.subplot(2,3,1)
plt.title("Plot-1")
plt.plot(x,y)

#plot2:
x=np.array([0,1,2,3])
y=np.array([55,20,50,40])
plt.subplot(2,3,2)
plt.title("Plot-2")
plt.plot(x,y)


#plot3:
x=np.array([0,1,2,3])
y=np.array([3,7,9,11])
plt.subplot(2,3,3)
plt.title("Plot-3")
plt.plot(x,y)

#plot4:
x=np.array([0,1,2,3])
y=np.array([3,12,14,10])
plt.subplot(2,3,4)
plt.title("Plot-4")
plt.plot(x,y)


#plot5:
x=np.array([0,1,2,3])
y=np.array([3,15,16,10])
plt.subplot(2,3,5)
plt.title("Plot-5")
plt.plot(x,y)

#plot6:
x=np.array([0,1,2,3])
y=np.array([3,18,17,10])
plt.subplot(2,3,6)
plt.title("Plot-6")
plt.plot(x,y)
plt.show()'''

'''
#creating scatter plots
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,2,3])
y = np.array([6,9,11,16,23])
colors=np.array([10,20,30,40,50])
plt.scatter(x,y,c=colors ,cmap='viridis')
plt.show()'''

'''import matplotlib.pyplot as plt
import numpy as np
x = np.array(["A","B","C"])
y = np.array([3,5,6])
plt.bar(x,y,color="yellow", width=0.3)
plt.show()'''


#histogram
'''import matplotlib.pyplot as plt
import numpy as np
x = np.random.normal(170, 10, 260)
plt.hist(x)
plt.show()'''

#piechart
'''
import numpy as np
import matplotlib.pyplot as plt
y=np.array([50,68,77,81])
plt.pie(y)
plt.show()'''

import matplotlib.pyplot as plt
import numpy as np
y=np.array([50, 68, 77, 81])
mylabels=['Apple', 'Mango', 'Guava', 'Kiwi']
myexplode=[0, 0, 0.1, 0]
plt.pie(y, labels=mylabels, startangle=120, explode=myexplode, shadow=True)
plt.legend(title="Different types of fruits:")
plt.show()








