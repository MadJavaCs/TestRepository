def MergeSort(arr):
    if len(arr) <=1:
        return arr


    middle = len(arr) // 2
    leftArr = MergeSort(arr[:middle])
    rightArr = MergeSort(arr[middle:])

    return Merge(leftArr,rightArr)


def Merge(leftArr,rightArr):
    sorted_arr = []
    i = 0
    j = 0

    while i < (len(leftArr)) and j < (len(rightArr)):
        if leftArr[i] <= rightArr[j]:
            sorted_arr.append(leftArr[i])
            i+=1
        else:
            sorted_arr.append(rightArr[j])
            j+=1


    sorted_arr.extend(leftArr[i:])
    sorted_arr.extend(rightArr[j:])

    return sorted_arr


arr = [2, 5, 7, 19, 20, 11, 20, 1, 3, 4, 6, 8, 99, 25, 210, 85, 79]
print(f"Orignal array: {arr}")
sorted_arr = MergeSort(arr)
print(f"Sorted array: {sorted_arr}")


