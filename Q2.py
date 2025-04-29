import numpy as np

# 6x6 array 0-35
matrix = np.arange(36).reshape(6,6)


# Borders = 1
matrix[0,:] = matrix[:,0] = matrix[-1,:] = matrix[:,-1] = 1


# Inside = 0
matrix[1:-1,1:-1] = 0
#print(matrix)


# 8x8 Checkerboard (0 value)   0 , 1
checkerboard = np.zeros((8,8), dtype=int)
checkerboard[1::2 , ::2] = 1
checkerboard[::2 , 1::2] = 1
#print(checkerboard)


# Rotate 90 degrees clockwise

rotated = np.rot90(checkerboard, k =-1)
print(rotated)