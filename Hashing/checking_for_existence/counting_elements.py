def counting_elements(arr):
    seen = set(arr)
    count = 0
    for i in range(len(arr)):
        x = arr[i]
        if x + 1 in seen:
            count += 1
    return count

