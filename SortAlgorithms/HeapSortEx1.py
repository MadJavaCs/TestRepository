def HeapSort(arr,n):
    n = len(arr)
    i = n//2-1
    for i in range(n//2-1, -1, -1):
        Heapify(arr,n,i)


    for i in range(n-1, 0, -1):
        arr[i],arr[0] = arr[0], arr[i]
        Heapify(arr,i,0)




def Heapify(arr,n,i):
    largest = i
    left = 2*i+1
    right = 2*i+2

    if left < n and arr[i] < arr[left]:
        largest = left


    if right < n and arr[largest] < arr[right]:
        largest = right


    if (largest!=i):
        arr[i], arr[largest] = arr[largest],arr[i]
        Heapify(arr,n, largest)














arr = [2,5,10,13,19,20,1,4,15,29,30,50]
n = len(arr)
print(f"Original array: {arr}")
HeapSort(arr,n)
print(f"Sorted array: {arr}")
