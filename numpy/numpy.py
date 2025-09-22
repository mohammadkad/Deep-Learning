'''
1404-06-31
Mohammad Kadkhodaei
'''

# Einstein notation:
# 1404-06-31
# ---
import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
# a.T
b = np.einsum('ij->ji', a)

# Create sample matrices
A = np.array([[1, 2, 3],   # Shape (2, 3)
              [4, 5, 6]])

B = np.array([[7, 8],      # Shape (3, 2)
              [9, 10],
              [11, 12]])

'''
A @ B
np.matmul(A, B)
'''
result_einsum = np.einsum('ij,jk->ik', A, B)
# ---
