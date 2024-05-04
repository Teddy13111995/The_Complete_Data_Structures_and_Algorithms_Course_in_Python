def insertion_sort(customList):
    for i in range(1,len(customList)):
        key = customList[i]
        j = i-1
        while j>=0 and key<customList[j]:
            customList[j+1]=customList[j]
            j=j-1
        customList[j+1]=key

    return customList

my_list = [54,84,10,2,1,3,5,9]

print(insertion_sort(my_list))