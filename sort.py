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

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left =  [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr


print(
    "Quick Sort:",                        quick_sort(arr),
    "\nMerge Sort:",                      merge_sort(arr),
    "\nBubble Sort:",                     bubble(arr),
    "\nInsertion Sort:",                  insertion(arr),
    "\nSelection sprt (Biggest End):",    Selection_biggestEND(arr),
    "\nSelection sort (Smallest First):", Selection_smallestFIRST(arr),
    "\nShell Sort:",                      shell_sort(arr)
)
