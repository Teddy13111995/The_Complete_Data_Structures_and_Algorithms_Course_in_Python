def swap(my_list, index_1, index_2):
    my_list[index_1], my_list[index_2] = my_list[index_2], my_list[index_1]


def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)

    swap(my_list, pivot_index, swap_index)
    return swap_index


def quick_sort(custom_list, left, right):
    if left < right:
        pivot_index = pivot(custom_list, left, right)
        quick_sort(custom_list, left, pivot_index - 1)
        quick_sort(custom_list, pivot_index + 1, right)

    return custom_list


my_list = [3,5,0,6,2,1,4]
print(quick_sort(my_list, 0, len(my_list) - 1))
# print(pivot(my_list,0,len(my_list)-1))
# print(my_list)