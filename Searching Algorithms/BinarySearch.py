def BinarySearch(target, list):
    list.sort()
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == list[mid]:
            return mid
        elif target > list[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1

target = 1
search_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("position : ", BinarySearch(target, search_list))