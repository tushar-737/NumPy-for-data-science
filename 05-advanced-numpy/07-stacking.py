import numpy as np
arr1=np.array([1,2,3,4])
arr2=np.array([5,6,7,8])
vertical_stack=np.vstack(((arr1,arr2)))
horizontal_stack=np.hstack(((arr1,arr2)))
print(vertical_stack)
print(horizontal_stack)