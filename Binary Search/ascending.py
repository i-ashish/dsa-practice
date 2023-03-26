"""Find an element in ascending sorted array."""
#Find 2 in sorted arr a

def ascending_element(arr,query):
    start = 0
    end = len(arr)-1

    while start <= end:
        mid = start + (end-start) // 2

        print(f"Start: {start}, End: {end}, middle: {mid}, Result: {arr[mid]}")

        if arr[mid] == query:
            return mid
    
        elif arr[mid] < arr[mid-1]:
            start = mid + 1

        else: end = mid -1

    return -1