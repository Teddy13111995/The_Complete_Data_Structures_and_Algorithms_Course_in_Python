import math
from insertion_sort import insertion_sort


def bucket_sort(customList):
    number_of_buckets = round(math.sqrt(len(customList)))
    # max = customList[0]
    # for i in range(1,len(customList)):
    #     if max < customList[i]:
    #         max = customList[i]
    max_value = max(customList)
    buckets = []
    for i in range(number_of_buckets):
        buckets.append([])
    for i in range(len(customList)):
        appropriate_bucket = math.ceil(customList[i] * number_of_buckets / max_value)
        buckets[appropriate_bucket - 1].append(customList[i])

    for j in range(number_of_buckets):
        buckets[j] = insertion_sort(buckets[j])

    # return_list = []
    # for i in range(number_of_buckets):
    #     for j in range(len(buckets[i])):
    #         return_list.append(buckets[i][j])
    #
    # return return_list

    k = 0
    for i in range(number_of_buckets):
        for j in range(len(buckets[i])):
            customList[k] = buckets[i][j]
            k = k + 1

    return customList


my_list = [54, 84, 10, 2, 1, 3, 5, 9]
print(bucket_sort(my_list))
