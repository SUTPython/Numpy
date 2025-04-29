import numpy as np

# Step 1: Create vectors
col_vector = np.arange(5).reshape(5,1)
row_vector = np.arange(5).reshape(1,5)

# print(col_vector)
# print(row_vector)


# Step 2: Add vectors
add = col_vector + row_vector
#print(add)

# Step 3: Multiply matrix by vector (column-wise)
matrix = np.arange(25).reshape(5,5)
#multiplied1 = matrix * col_vector
multiplied2 = matrix * row_vector
#print(multiplied1)
#print(multiplied2)



# Step 4: Add scalar

scalar_added = matrix + 10
print(scalar_added)
