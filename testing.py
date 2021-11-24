import copy

A = [1, 2, 3, 4, 5, 6, 7, 8]

for i in reversed(range(len(A))):
    A[i] *= -1 

print(A)