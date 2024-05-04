def linear_search(custom_list, element_to_be_searched):
    for i in range(len(custom_list)):
        if custom_list[i] == element_to_be_searched:
            return i
    return -1

my_list = [54, 84, 10, 2, 1, 3, 5, 9]
print(linear_search(my_list, 100))
