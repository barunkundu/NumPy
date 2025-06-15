import numpy as np 

''' check NumPy version'''
# print(np.__version__)


# make a 3D array
array_3D = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [1,2,3]]])
print(array_3D)



# matrix = np.array([[1,2,3,4],
#                   [5,6,7,8]])
# print(matrix)

""" use the default value to make matrix"""
# # fill with "0"
# fill_o = np.zeros((2,3))
# print(fill_o)

# # fill with one(1)
# fill_ones = np.ones((2,2))
# print(fill_ones)

# # fill with specific value
# fill_specific = np.full((2,3), 5)
# print(fill_specific)

""" create Sequence of number Using arange function"""
''' function model: numpy.arange(start, stope, step)'''
# seq = np.arange(1, 20, 3)
# print(seq)

''' make identity matrix use of function "eye(shape)" '''
# identity_mat = np.eye(3)
# print(identity_mat)
