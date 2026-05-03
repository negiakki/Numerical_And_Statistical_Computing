import numpy as np

A = np.array([[10, -1, 2],
              [-1, 11, -1],
              [2, -1, 10]])

B = np.array([6, 25, -11])
x = np.zeros(3)

for _ in range(25):
    x_new = np.zeros(3)
    for i in range(3):
        s = sum(A[i][j]*x[j] for j in range(3) if j != i)
        x_new[i] = (B[i] - s) / A[i][i]
    x = x_new

print(x)
