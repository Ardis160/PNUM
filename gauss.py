import numpy as np

a = np.array([[2, 2, 0],
              [2, 4, 0],
              [1, 0, 2]], float)

b = np.array([5, 3, 7], float)

n = len(b)
for k in range(n):
    for i in range(k + 1, n):
        fctr = a[i, k] / a[k, k]
        for j in range(k, n):
            a[i, j] -= fctr * a[k, j]
        b[i] -= fctr * b[k]

# Zpětná substituce
x = np.zeros(n)
for i in range(n - 1, -1, -1):
    x[i] = (b[i] - np.dot(a[i, i + 1:], x[i + 1:])) / a[i, i]

print("Koeficienty jsou")
print(x)
