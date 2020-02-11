#!/usr/bin/python36
import sys
print("Python version")
print (sys.version)

grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1],[0,0,0,0]]
row=grid[0]
print (grid[0])
num_row = print(len(row))
print("Number Rows:%s" % num_row)

# target = 22
# for x in range(len(A)):
#     diff = target - A[x]
#     if diff > 0:
#         try:
#             value_index = A.index(diff)
#         except:
#             value_index = -1
#     if value_index > 1:
#         print(x)
#         print(value_index)