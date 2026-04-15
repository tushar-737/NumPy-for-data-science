import numpy as np
arr=np.array([1,2,np.nan,4,np.nan,5,7])
cleaned_arr1=np.nan_to_num(arr)
cleaned_arr2=np.nan_to_num(arr,nan=100)
print(cleaned_arr1)
print(cleaned_arr2)
