"""Find an element in sorted rotated array."""

#First find index of smallest element in the array which will divide array into two sorted array and then search for element in both arrays.
def main(arr, query):
    
    smallest = smallest_element(arr)
    last = len(arr) - 1

    res1 = binary_search(arr,0,smallest-1, query)
    res2 = binary_search(arr, smallest , last, query)

    if res1 == -1:
        return res2

    else: return res1


    
def smallest_element(arr):
    start = 0
    end = len(arr)-1
    N = len(arr)

    while start <= end:
        
        mid = start + (end-start) // 2
        prev = (mid + N -1) % N
        nxt = (mid + 1) % N

        if arr[prev] > arr[mid] < arr[nxt]:
            return mid

        elif arr[mid] > arr[end]:
            start = mid + 1

        else: end = mid - 1

    return -1

def binary_search(arr,start, end, query):

    while start <= end:
        middle = start + (end-start) // 2

        if arr[middle] == query:
            return middle

        elif arr[middle] < query:
            start = middle + 1

        else: end = middle -1

    return -1

if __name__ == "__main__":
    
    arr = [11,12,15,18,2,5,6,8]
    query = 18
    print(main(arr, query))