def insertInList():
    my_list = [1, 2, 3, 4, 5, 6]
    print(my_list)
    my_list.insert(2, 10)
    print(my_list)
    my_list.append(7)
    my_list_2 = [11, 12, 13]
    my_list.extend(my_list_2)
    print(my_list)


# list slicing
def slicingList():
    my__list = ['a', 'b', 'c']
    print(my__list[0:2])
    print(my__list[1:])


# deletion
def deletionInList():
    my_list_3 = ['a', 'b', 'c', 'd', 'e']
    my_list_3.pop(2)
    print(my_list_3)
    del my_list_3[2:3]
    print(my_list_3)
    my_list_3.remove('b')
    print(my_list_3)


def searchingInList():
    my_list = [10, 20, 30, 40, 50, 60, 70, 80]
    target = 50
    if target in my_list:
        print(f'{target} in list')
    else:
        print(f'{target} not in list')
    print(linearSearch(my_list, target))


def linearSearch(p_list, p_target):
    for i, value in enumerate(p_list):
        if value == p_target:
            return i
    return -1


if __name__ == '__main__':
    searchingInList()
