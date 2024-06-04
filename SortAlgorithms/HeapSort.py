def HeapSort(arr,n):
    n = len(arr)
    i = n//2-1
    for i in range(n//2, -1, -1):
        Heapify(arr,n,i)


    for i in range(n-1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i]
        Heapify(arr,i,0)




def Heapify(arr,n,i):

    left = 2*i +1
    right = 2*i + 2
    largest = i

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right


    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        Heapify(arr, n, largest)







arr = [2, 5, 7, 19, 20, 11, 20, 1, 3, 4, 6, 8, 99, 25, 210, 85, 79]
n = len(arr)
print(f"Original array: {arr}")
HeapSort(arr,n)
print(f"Sorted array: {arr}")