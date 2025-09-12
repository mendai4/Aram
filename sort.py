arr = [ 5, 8, 3, 4, 8, 1 ]
n = len(arr)

def bubble(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def insertion(arr):
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def Selection_biggestEND(arr):
    for i in range(n - 1, -1, -1):
        maxid = i
        for j in range(0, i):
            if arr[j] > arr[maxid]:
                maxid = j
        arr[i], arr[maxid] = arr[maxid], arr[i]
    return arr

def Selection_smallestFIRST(arr):
    for i in range(n):
        minid = i
        for j in range(i + 1, n):
            if arr[j] < arr[minid]:
                minid = j
        arr[i], arr[minid] = arr[minid], arr[i]
    return arr


print(
    bubble(arr),
    insertion(arr),
    Selection_biggestEND(arr),
    Selection_smallestFIRST (arr)
    )