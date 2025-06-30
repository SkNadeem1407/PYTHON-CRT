'''import numpy as np
arr = np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
print(arr[0,1,2])
print(arr[])'''

'''#2d slicing:
import numpy as np
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[1, 1:4])'''

''''#copy
import numpy as np
arr = np.array([1,2,3,4,5])
x = arr.copy()
arr[0]=42
print(arr)
print(x)'''

'''#view
import numpy as np
arr = np.array([1,2,3,4,5])
x = arr.view()
arr[0]=42
print(arr)
print(x)'''

'''#array shape
import numpy as np
arr = np.array([[1,2,3,4],[5,6,7,8]])
print(arr.shape)'''

'''#array reshape
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
newarr=arr.reshape(5,3,1)
print(newarr)'''

'''#array iterating 2d
import numpy as np
arr=np.array[]
'''

'''#array iteration 3d
import numpy as np
arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for x in arr:
    print(x)
print(arr[0,1:4])'''

'''#joinig two arrays:
import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.concatenate((arr1,arr2))
print(arr)'''

'''#joining two arrays 2d
import numpy as np
arr1 = np.array([[1,2], [3,4]])
arr2 = np.array([[5,6], [7,8]])
arr = np.concatenate((arr1,arr2),axis=1)
print(arr)'''

'''#joining two arrays 2d
import numpy as np
arr1 = np.array([[1,2], [3,4]])
arr2 = np.array([[5,6], [7,8]])
arr = np.concatenate((arr1,arr2),axis=0)
print(arr)'''

'''import numpy as np
revenue=np.array([20000,22000,21000,25000,24000])
avg=sum(revenue)/len(revenue)
print(avg)'''

'''import numpy as np
scores=np.array([45,67,89,76,65])
count=0
for x in scores:
    if (x>60):
        count+=1
print(count)'''

'''import numpy as np
prices=np.array([50,20,30])
quantities=np.array([2,5,3])
total_bill=prices*quantities
print(total_bill)'''

'''import numpy as np
ratings=np.array([4,3,5,2,5,3,4,5,1])
count=0
for x in ratings:
    if (x==5):
        count+=1
print(count)'''

import numpy as np
houses_prices=np.array([45,50,48,52,47])
new_price=(houses_prices*0.10)+houses_prices
print(new_price)



