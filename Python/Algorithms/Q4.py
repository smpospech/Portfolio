import time
import numpy as np

n = input("enter a value: ")

n = int(n)

a = np.zeros(((n+1), (n+1)), dtype=int)
b = np.zeros(((n+1), (n+1)), dtype=int)
c = np.zeros(((n+1), (n+1)), dtype=int)

for i in range(1,n):
    for j in range(1,n):
        print(a[i][j])


