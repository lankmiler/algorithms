arr = [30, 60, 20, 50, 40, 10]

# [10, 30, 60, 20, 50, 40]

for key in range(0, len(arr) - 1):
    arr_sliced = arr[key+1:]
    min_value = min(arr_sliced)
    min_index = arr.index(min_value)
    if arr[key] > arr[min_index]:
        arr[key], arr[min_index] = arr[min_index], arr[key]

# print(arr)

