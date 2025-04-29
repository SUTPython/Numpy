import numpy as np


# Step 1: Two random 3x3 matrices
A = np.random.randint(0,10,(3,3))
B = np.random.randint(0,10,(3,3))
# print(A)
# print(B)

# Step 2a: Addition
add = A + B
#print(add)

# Step 2b: Element-wise multiplication
multiply1 =  A * B
#print(multiply1)


# Step 2c: Matrix multiplication (dot product)
multiply2 = A @ B
#print(multiply2)

# Step 2d: Determinant
det_A = np.linalg.det(A)
print(det_A)

# Step 2e: Inverse
if np.abs(det_A) > 1e-6:
    inv_A = np.linalg.inv(A)
    print(inv_A)
else:
    print("matrix A is singular, no inverse")
