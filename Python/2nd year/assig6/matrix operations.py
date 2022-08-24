import numpy as np
#python program to create matrix
a = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
b = np.array([[3, 3, 3], [2, 2, 2], [1, 1, 1]])
print(a)
#python program to Add two matrices
print(a+b)
#python program to multiply two matrices
print(np.dot(a, b))
#python program to transpose given matrix
x = np.transpose(a)
print(x)
#Given a square matrix of N rows and columns, find out whether it is symmetric or not.
comp = a == x
if(comp.all()):
    print("symmetric")
else:
    print("asymmetric")
#Python program to find row-wise maximum element of matrix
for i in range(0, len(a)):
    print(np.max(a[i]))
#Python program to element wise matrix addition,subtraction and division
print(a+b)
print(a-b)
print(a/b)





