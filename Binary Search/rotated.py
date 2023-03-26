"""
How many times a sorted array is rotated.
I/P: arr = [11,12,15,18,2,5,6,8]
O/P: 4
"""
#Number of time an array is rotated == Index of smallest element

"""For mid to be smallest in the array - element will be smaller than both its neighbours."""

def rotated_arr(arr):

    start = 0
    end = len(arr)-1
    N = len(arr)

    while start <= end:
        mid = start + (end-start) // 2

        prev = (mid + N -1) % N
        next = (mid + 1) % N

        #print(f"Start: {start}, End: {end}, Mid: {mid}, Result: {arr[mid]}")
        #print(f"Previous element: {prev}, Next element: {next}")

        if arr[prev] > arr[mid] < arr[next]:
            return mid
        
        elif arr[mid] > arr[end]:
            start = mid + 1

        else: end = mid -1

    return -1 

arr1 = [11,12,15,18,2,5,6,8]
print(rotated_arr(arr1)) #O/P - 4

arr2 = [10,2,4,6,8]
print(rotated_arr(arr2)) #O/P - 1