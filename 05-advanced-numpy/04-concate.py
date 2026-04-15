import numpy as np
arr1=np.array([1,2,3,4])
arr2=np.array([5,6,7,8])
new1=np.concat((arr2,arr1))
new2=np.concat((arr1,arr2))
print(new1)
print(new2)