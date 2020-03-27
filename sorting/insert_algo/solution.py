arr = [7, 5, 6, 4, 9, 8, 2, 1, 3]
result_arr = [arr[0]]


for item in range(0, len(arr)):
    for key in range(0, len(result_arr)):
        if len(result_arr) == 1:
            if result_arr[key] > arr[item]:
                temp = result_arr[key]
                result_arr.append(temp)
                result_arr[0] = arr[item]
                break
        elif result_arr[key] < item < result_arr[key + 1]:
            result_arr.insert(key + 1, item)
            break

print(result_arr)