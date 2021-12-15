import numpy as np
A=np.array([[2,3,6],[3,4,5],[6,5,9]])
B=np.array([[0,2,9],[-2,0,3],[-9,-3,0]])
AT=A.transpose()
comparison = A == AT
equal_arrays = comparison.all()
print(equal_arrays)
m=(B.transpose() == -B).all()
print(m)