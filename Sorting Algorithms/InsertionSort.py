def insertion_sort(arr):
    length_arr = len(arr)
    for i in range(1, length_arr):
        store = arr[i] 
        j = i - 1
        while arr[j] > store and j > -1:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = store