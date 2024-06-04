def SelectionSort(arr):
    n = len(arr)
    for i in range(0,n-1):
        min = i
        j = i + 1
        for j in range(i+1, n):
            if arr[j] < arr[min]:
                min = j

        arr[i], arr[min] = arr[min], arr[i]









arr = [5,9,10,1,4,3,2,6,8,7,11,14,13,29,68,59,100,102,200,359,232,15,12,22,21,29,58,48,38]
print(f"Original array: {arr}")
SelectionSort(arr)
print(f"Sorted array: {arr}")