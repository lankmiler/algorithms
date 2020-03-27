arr = [30, 60, 20, 50, 40, 10]

for key in range(0, len(arr) - 1):
    arr_sliced = arr[key+1:]
    max_value = max(arr_sliced)
    max_index = arr.index(max_value)
    if arr[key] < arr[max_index]:
        arr[key], arr[max_index] = arr[max_index], arr[key]

print(arr)

