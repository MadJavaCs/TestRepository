def insertionsort(beispielarray):
    for i in range(1, len(beispielarray)):
        temp = beispielarray[i]
        j = i-1

        while j>=0 and beispielarray[j] > temp:
            beispielarray[j+1] = beispielarray[j]
            j -= 1

        beispielarray[j+1] = temp


beispielarray = [42,77,6,31,14,6,77,468,42000,15]
insertionsort(beispielarray)
print(beispielarray)