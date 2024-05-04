def merge(customList, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = customList[left + i]

    for j in range(0, n2):
        R[j] = customList[mid + 1 + j]

    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            customList[k] = L[i]
            i += 1
        else:
            customList[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        customList[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        customList[k] = R[j]
        j += 1
        k += 1


def merge_sort(customList, left, right):
    if left < right:
        mid = (left + (right - 1)) // 2
        merge_sort(customList, left, mid)
        merge_sort(customList, mid + 1, right)
        merge(customList, left, mid, right)
    return customList


my_list = [54, 84, 10, 2, 1, 3, 5, 9]
print(merge_sort(my_list, 0, len(my_list) - 1))
