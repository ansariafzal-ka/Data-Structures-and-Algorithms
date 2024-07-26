def LinearSearch(target, list):
    position = 0
    for item in list:
        if item == target:
            return position
        position += 1
    return None

search_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 10

print("position : ",LinearSearch(target, search_list))