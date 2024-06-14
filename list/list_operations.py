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
    a = [0]*4
    print(a)

    # len() - count number of elements
    a = [1,2,3,4,5]
    print(len(a))

    #max() - find maximum element in list
    print(max(a))
    #min() - find minimum element in list
    print(min(a))
    #sum() - find sum of elements in a list
    print(sum(a))

def average_using_list():
    my_list = []


if __name__ == '__main__':
    list_functions()
