import numpy as np
# a = np.array([1,2,3,4,5])
# print (type(a))
# print(a.shape)
# print(a[0], a[1], a[2], a[3], a[4])

# a=np.array([[1,2,3],[4,5,6]])
# print(a.shape)
# a=np.zeros((2,2))
# nb=np.ones((1,2))
# c=np.full((2,2),7)
# d=np.random.random((2,2))
# print(a.dtype)
x=np.array([[1,2],[3,4]],dtype=np.float64)
y=np.array([[5,6],[7,8]],dtype=np.float64)
print(x+y)