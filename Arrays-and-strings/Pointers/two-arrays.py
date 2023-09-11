def sorted_array(arr1, arr2):
    i = 0
    j = 0
    ans = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[i]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j += 1
            
    while i < len(arr1):
        ans.append(arr1[i])
        i += 1
        
    while j < len(arr2):
        ans.append(arr2[j])
        j += 1
        
    return ans


arr1 = [1, 2, 3, 4, 14]
arr2 = [6, 7, 8, 9, 10, 11]

print(sorted_array(arr1, arr2))