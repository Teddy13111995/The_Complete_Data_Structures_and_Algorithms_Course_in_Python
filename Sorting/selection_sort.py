def selection_sort(customList):
    for i in range(len(customList)):
        pos = i
        for j in range(i + 1, len(customList)):
            if customList[pos] > customList[j]:
                pos = j
        customList[i], customList[pos] = customList[pos], customList[i]
    return customList


my_list = [54, 84, 10, 2, 1, 3, 5, 9]
print(selection_sort(my_list))
