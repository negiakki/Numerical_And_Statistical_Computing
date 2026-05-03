import numpy as np

A = np.array([[2.0, 1.0, -1.0],
              [-3.0, -1.0, 2.0],
              [-2.0, 1.0, 2.0]])

B = np.array([8.0, -11.0, -3.0])

n = len(B)

for i in range(n):
    for j in range(i+1, n):
        ratio = A[j][i] / A[i][i]
        for k in range(n):
            A[j][k] -= ratio * A[i][k]
        B[j] -= ratio * B[i]

x = np.zeros(n)
for i in range(n-1, -1, -1):
    x[i] = (B[i] - sum(A[i][j]*x[j] for j in range(i+1, n))) / A[i][i]

print(x)
