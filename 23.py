import numpy as np
A = np.array([[1,2],[3,4]])
B = np.array([[2,3],[4,5]])
print(A, B)
print("Addition: A + B = \n", A+B)
print("SUbtraction: A-B =\n", A-B)


C = np.array([[2,3],[4,5]])
vector = np.array([1,2])
print("Add: ", C+ vector)


print("sum: ", np.sum(C))