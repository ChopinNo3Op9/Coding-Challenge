def consecutive_increasing_indices(arr):
    consecutive_indices = []
    current_run = [arr[0]]

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            current_run.append(arr[i])
        else:
            if len(current_run) > 1:
                consecutive_indices.append(current_run)
            current_run = [arr[i]]

    if len(current_run) > 1:
        consecutive_indices.append(current_run)

    return consecutive_indices

# test
my_list = [1, 2, 3, 5, 1, 1, 1, 7, 15, 11, 12]
# my_list = [1, 1, 1, 1]
result = consecutive_increasing_indices(my_list)
print(result)
