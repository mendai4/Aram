import math
arr1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 22, 25, 26, 31, 36, 37, 37, 40]
a = 15

def linear_search(arr1, a):
    for i in range(len(arr1)):
        if arr1[i] == a:
            return i
    return "not found"

def binary_search(arr1, a):
    l = 0
    h = len(arr1) - 1

    while l <= h:
        mid = (l + h) // 2
        if arr1[mid] == a:
            return mid
        elif arr1[mid] < a:
            l = mid + 1
        else:
            h = mid - 1
    return "not found"

def ternary_search(arr1, a):
    l = 0
    h = len(arr1) - 1
    
    while l <= h:
        mid1 = l + (h - l) // 3
        mid2 = h - (h - l) // 3
        
        if arr1[mid1] == a:
            return mid1
        if arr1[mid2] == a:
            return mid2
        if a < arr1[mid1]:
            h = mid1 - 1
        elif a > arr1[mid2]:
            l = mid2 + 1
        else:
            l = mid1 + 1
            h = mid2 - 1
    return "not found"

def jump_search(arr1, a):
    m = len(arr1)
    step = int(math.sqrt(m))
    prev = 0
    
    while prev < m and arr1[min(step, m) - 1] < a:
        prev = step
        step += int(math.sqrt(m))
        if prev >= m:
            return -1
    for i in range(prev, min(step, m)):
        if arr1[i] == a:
            return i
    return "not found"

def interpolation_search(arr1, a):
    low, high = 0, len(arr1) - 1
    while low <= high and arr1[low] <= a <= arr1[high]:
        if arr1[low] == arr1[high]:
            return low if arr1[low] == a else -1
        pos = low + (high - low) * (a - arr1[low]) // (arr1[high] - arr1[low])
        if arr1[pos] == a:
            return pos
        if arr1[pos] < a:
            low = pos + 1
        else:
            high = pos - 1
    return "not found"

def exponential_search(arr1, a):
    i = 1
    m = len(arr1)
    
    if arr1[0] == a:
        return 0
    while i < m and arr1[i] <= a:
        i *= 2
    return binary_search(arr1[:min(i, m)], a)

print("linear: ", linear_search(arr1, a))
print("binary: ", binary_search(arr1, a))
print("ternary: ", ternary_search(arr1, a))
print("jump: ", jump_search(arr1, a))
print("interpolation: ", interpolation_search(arr1, a))
print("exponential: ", exponential_search(arr1, a))