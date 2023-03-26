"""Find an element in descending sorted array."""
#Find 4 in decending sorted array.

def descending_element(arr,a):
    start = 0
    end = len(arr)-1
    
    while start <= end:
        mid = start + (end-start) // 2
        print(f"Start: {start}, End: {end}, middle: {mid}, Result: {arr[mid]}")

        if arr[mid] == a:
            return mid

        elif arr[mid] < arr[mid-1]:
            start = mid + 1

        else: end = mid - 1

    return -1
