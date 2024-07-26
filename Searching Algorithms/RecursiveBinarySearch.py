def RecursiveBinarySearch(target, list):
    if not list:
        return False
    mid_point = (len(list) - 1) // 2
    if target == list[mid_point]:
        return True
    else:
        if target > list[mid_point]:
            return RecursiveBinarySearch(target, list[mid_point + 1:])
        else:
            return RecursiveBinarySearch(target, list[:mid_point])
    
search_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(RecursiveBinarySearch(8, search_list))