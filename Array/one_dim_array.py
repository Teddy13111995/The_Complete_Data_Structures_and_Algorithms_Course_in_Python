from array import *

# Create an array and traverse

my_array = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])

for i in range(len(my_array)):
    print(my_array[i], end=' ')

# access individual elements through indexes
print(my_array[1], my_array[4], my_array[7])
# append any value to array using append()
my_array.append(10)
print(my_array)
# insert value in the array using insert()
my_array.insert(4,14)
print(my_array)
# extend python array using extend()
my_array.extend([11,12,13,15,16])
print(my_array)
# add items from list into array using fromlist()
my_array.fromlist([17,18,19,20])
print(my_array)
