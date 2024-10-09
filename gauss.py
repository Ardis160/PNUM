import numpy as np

a = np.array([[2, 2, 0],
              [2, 4, 0],
              [1, 0, 2]], float)

b = np.array([5, 3, 7], float)

n = len(b)

for i in range(n):
    for j in range(i + 1, n):
        multiplier = a[j, i] / a[i, i]
        for k in range(i, n):
            a[j, k] -= multiplier * a[i, k]
        b[j] -= multiplier * b[i]

print(a)

x = np.zeros(n)

for i in range(n - 1, -1, -1):
    x[i] = (b[i] - np.dot(a[i, i + 1:], x[i + 1:])) / a[i, i]

print("Koeficienty jsou")
print(x)

"""
y = np.linalg.solve(a, b)

print("Koeficienty jsou:")
print(y)"""

