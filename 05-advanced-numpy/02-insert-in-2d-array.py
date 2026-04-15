import numpy as np
arr=np.array([[1,2],[2,3]])
print(arr)
new_arr1=np.insert(arr,2,[3,4],axis=1)#axis=1 (column wise)
new_arr2=np.insert(arr,2,[3,4],axis=0)#axis=0 (row wise)
print(new_arr1)
print(new_arr2)