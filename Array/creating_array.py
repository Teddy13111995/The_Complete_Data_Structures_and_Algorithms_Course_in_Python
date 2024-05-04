from array import *

my_array = array('i',[1,2,3,4])

print(my_array)
#
# import numpy as np
#
# np_array = np.array(['1','2','3','4','5'])
# print(np_array)

# Insertion in an array
# at beginning
my_array.insert(0,6)
print(my_array)

# in middle
my_array.insert(len(my_array)//2,6)
print(my_array)

# at end
my_array.insert(len(my_array),6)
print(my_array)

# array traversal
def array_traversal(array):
    for i in array:
        print(i)

array_traversal(my_array)