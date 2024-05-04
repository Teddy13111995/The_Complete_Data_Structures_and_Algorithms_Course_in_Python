def bubble_sort(customList):
    for i in range(len(customList)-1):
        for j in range(len(customList)-i-1):
            if customList[j]>customList[j+1]:
                (customList[j],customList[j+1])=(customList[j+1],customList[j])
    return customList

my_list = [54,84,10,2,1,3,5,9]

print(bubble_sort(my_list))