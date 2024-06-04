def partition(beispielarray, links, rechts):
    pivot = beispielarray[rechts]
    i = links - 1

    for j in range(links, rechts):
        if beispielarray[j] <= pivot:
            i += 1
            beispielarray[i], beispielarray[j] = beispielarray[j], beispielarray[i]

    beispielarray[i+1], beispielarray[rechts] = beispielarray[rechts], beispielarray[i+1]
    return i + 1

def quicksort(beispielarray, links, rechts):
    if links < rechts:
        pivotIdx = partition(beispielarray, links, rechts)
        quicksort(beispielarray, links, pivotIdx - 1)
        quicksort(beispielarray, pivotIdx + 1, rechts)

beispielarray = [42, 77, 6, 31, 14, 6, 77, 468, 42000, 15]
quicksort(beispielarray, 0, len(beispielarray) - 1)
print(beispielarray)