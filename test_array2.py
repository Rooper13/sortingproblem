import numpy as np 
#0 D proses
arr = np.array(42)

print(arr)

#first dimension
arr2 = np.array([1,2,3,4,5])
print (arr2)


#2d array

arr3 = np.array([[1, 2, 3], [4, 5, 6]])
print (arr3)


#3d array

arr4 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr4)

#check number 

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)