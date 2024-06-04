def partition(arr,low,high):
    pivot = arr[high]
    i = low-1

    for j in range(low,high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j],arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i + 1



def quick_sort(arr,low,high):
    if low < high:
        pivotIdx = partition(arr,low,high)
        quick_sort(arr,low,pivotIdx-1)
        quick_sort(arr,pivotIdx+1,high)






arr = [2,59,10,11,10,3,1,4,5,6,29,19,200,48,657,159,199,78,105,99,101,7,8]
print(f"Original array: {arr}")
quick_sort(arr,0,len(arr)-1)
print(f"Sorted array: {arr}")

