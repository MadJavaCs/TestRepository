def MergeSort(arr):

    if len(arr) <= 1:
        return arr

    middle = len(arr)//2
    leftArr = MergeSort(arr[:middle])
    rightArr = MergeSort(arr[middle:])

    return Merge(leftArr, rightArr)

def Merge(leftArr, rightArr):
    sorted_arr = []
    i = 0
    j = 0

    while i < len(leftArr) and j < len(rightArr):
        if leftArr[i] <= rightArr[j]:
            sorted_arr.append(leftArr[i])
            i+=1
        else:
            sorted_arr.append(rightArr[j])
            j+=1

    sorted_arr.extend(leftArr[i:])
    sorted_arr.extend(rightArr[j:])

    return sorted_arr


arr = [4,6,92,19,10,18,200,52,3,1,5,7,9,11,13,14,16,25,30]
print("Original array:", arr)
sorted_arr =MergeSort(arr)
print("Sorted array:", sorted_arr)
