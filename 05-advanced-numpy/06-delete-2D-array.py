import numpy as np
arr=np.array([[1,2,3,4],[5,6,7,8]])
print(arr)
print("new: ")
new1=np.delete(arr,0,axis=0)#horizontal
new2=np.delete(arr,0,axis=1)#vertical
print(new1)
print(new2)