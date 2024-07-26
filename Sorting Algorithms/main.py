def two_sum(arr, target):
    # for(int i = 0, i < arr.length -1; i++)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]

arr = [1, 5, 0, 9]
target = 10
print(two_sum(arr, target))