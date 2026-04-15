import numpy as np
arr=np.array([1,2,3,4,5,6])
print(arr)
new_arr=np.insert(arr,2,7,0) #insert(array_name,index,value,axis)
print(new_arr)