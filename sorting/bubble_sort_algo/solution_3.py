arr = [7, 5, 6, 4, 9, 8, 2, 1, 3]

swapped = True
while swapped:
    swapped = False
    for item in range(0, len(arr) - 1):
        if(arr[item] > arr[item + 1]):
            arr[item], arr[item + 1] = arr[item + 1], arr[item]
            swapped = True
print(arr)