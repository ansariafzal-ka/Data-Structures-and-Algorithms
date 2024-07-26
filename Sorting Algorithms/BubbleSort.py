def bubble_sort(list):
    list_length = len(list)
    for i in range(list_length - 1):
        for j in range(list_length - 1 - i):
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp