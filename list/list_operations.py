import random


def insert_in_list():
    my_list = [1, 2, 3, 4, 5, 6]
    print(my_list)
    my_list.insert(2, 10)
    print(my_list)
    my_list.append(7)
    my_list_2 = [11, 12, 13]
    my_list.extend(my_list_2)
    print(my_list)


# list slicing
def slicing_list():
    my__list = ['a', 'b', 'c']
    print(my__list[0:2])
    print(my__list[1:])


# deletion
def deletion_in_list():
    my_list_3 = ['a', 'b', 'c', 'd', 'e']
    my_list_3.pop(2)
    print(my_list_3)
    del my_list_3[2:3]
    print(my_list_3)
    my_list_3.remove('b')
    print(my_list_3)


def searching_in_list():
    my_list = [10, 20, 30, 40, 50, 60, 70, 80]
    target = 50
    if target in my_list:
        print(f'{target} in list')
    else:
        print(f'{target} not in list')
    print(linear_search(my_list, target))


def linear_search(p_list, p_target):
    for i, value in enumerate(p_list):
        if value == p_target:
            return i
    return -1


def list_functions():
    # + operator - concatenate 2 list
    list_1 = [10, 20, 30]
    list_2 = [40, 50, 60]
    my_list = list_1 + list_2
    print(my_list)
    # * operator - repeat element n times
    a = [0] * 4
    print(a)

    # len() - count number of elements
    a = [1, 2, 3, 4, 5]
    print(len(a))

    # max() - find maximum element in list
    print(max(a))
    # min() - find minimum element in list
    print(min(a))
    # sum() - find sum of elements in a list
    print(sum(a))


def average_using_list():
    my_list = list()
    while True:
        inp = input('Enter a number')
        if inp == 'done': break
        my_list.append(int(inp))
    average = sum(my_list) / len(my_list)
    return average


def list_from_string():
    a = 'spam'
    b = list(a)
    print(b)
    a = 'using split function'
    b = list(a.split(' '))
    print(b)
    a = 'using-delemiter-function'
    b = a.split('-')
    print(b)

    print('-'.join(b))


def list_pitfall():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8]
    my_list = my_list.sort()  # my_list becomes None
    my_list = [1, 2, 3, 4, 5, 6, 7, 8]
    my_list.append([10])  # appends list to another list
    # make a copy
    copied_list = my_list[:]
    # using sorted(my_list) doesn't alter list


def list_vs_arrays():
    """
    Similarities
    1. Both data structure are mutable
    2. Both can be indexed and iterated through
    3. They can be both sliced

    Differences
    1. array is used for arithmetic operations
    2. list elements can have different data types

    """
    import numpy as np
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    new_list = np.array(my_list)

    print(new_list / 2)
    print(my_list / 2)
    pass


def tc_sc_list():
    """
    op                              tc      sc
    creating an empty list          O(1)    O(1)
    creating a list with elements   O(n)    O(n)
    inserting a value in list       O(n)    O(1)
    traversing a list               O(n)    O(1)
    accessing a given cell          O(1)    O(1)
    searching a given value         O(n)    O(1)
    deleting a value from list      O(1)    O(1)
    """
    pass


def list_comprehension():
    prev_list = [1, 2, 3]
    # new_list = [new_item for item in list]
    new_list = [2 * x for x in prev_list]
    print(new_list)

    str_ = 'python'
    list_char = [x for x in str_]
    print(list_char)
    "list comprehension can be used for list, range, string and tuple"


def conditional_list_comprehension():
    # new_list = [new_item for item in list if condition]
    prev_list = [-1, 10, -20, 2, -90, 60, 45, 20]
    new_list = [num for num in prev_list if num > 0]
    print(new_list)
    new_list = [num ** 2 for num in prev_list if num < 0]
    print(new_list)

    pass


def string_list_comprehension():
    def is_consonant(letter):
        vowels = 'aeiou'
        return letter.isalpha() and letter.lower() not in vowels

    sentence = 'my name is srijan'
    consonants = [letter for letter in sentence if is_consonant(letter)]
    print(consonants)

    # new_list = [ new_item if condition for item in list]
    new_list = ['apple','banana','mango']
    random.shuffle(new_list)
    print(new_list)

    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(a[::2])

    # a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # a[::2] = 10, 20, 30, 40, 50, 60
    # print(a)


if __name__ == '__main__':
    string_list_comprehension()
