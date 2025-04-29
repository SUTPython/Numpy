import numpy as np

#1- 10 * 10 random matrix
matrix = np.random.randint(0,101,(10,10))
#print(matrix)

#2- Even number -> -1
matrix[matrix % 2 == 0] = -1


#3- Numbers > 50 -> 999
matrix[matrix > 50] = 999
print(matrix)