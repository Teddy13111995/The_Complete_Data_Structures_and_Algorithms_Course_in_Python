def heapify(custom_list, no_of_elements, current_index):
    smallest = current_index
    left_child = 2 * current_index + 1
    right_child = 2 * current_index + 2
    if left_child < no_of_elements and custom_list[left_child] < custom_list[smallest]:
        smallest = left_child

    if right_child < no_of_elements and custom_list[right_child] < custom_list[smallest]:
        smallest = right_child

    if smallest != current_index:
        custom_list[current_index], custom_list[smallest] = custom_list[smallest], custom_list[current_index]
        heapify(custom_list, no_of_elements, smallest)


def heap_sort(custom_list):
    n = len(custom_list)
    for i in range(int(n / 2) - 1, -1, -1):
        heapify(custom_list, n, i)

    for i in range(n - 1, 0, -1):
        custom_list[i], custom_list[0] = custom_list[0], custom_list[i]
        heapify(custom_list, i, 0)

    custom_list.reverse()
    return custom_list


my_list = [3, 5, 0, 6, 2, 1, 4]
print(heap_sort(my_list))