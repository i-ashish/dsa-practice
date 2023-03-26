""" In a sorted list find first and last occurence of element.
search = 10
arr = [2,4,10,10,10,18,20]
"""
#O/P: 1st occurence = 2, last occurence =4

def first_occur(arr,query):
    start = 0
    end = len(arr)-1

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == query:
            res = mid
            end = mid -1

        elif arr[mid]>arr[mid-1]:
            start = mid+1

        else: end = mid-1
    return res

def last_occur(arr,query):

    start = 0
    end = len(arr)-1

    while start <= end:
        mid = start + (end - start) // 2

        #print(f"Start: {start}, End: {end}, Mid: {mid}, Result: {arr[mid]}")

        if arr[mid] == query:
            res = mid
            start = mid + 1

        elif arr[mid]<query:
            start = mid+1

        else: end = mid-1
    return res

arr = [2,4,10,10,10,18,20]
query = 10
#print(f"1st occurence of {query} in array {arr} is: {first_occur(arr,query)}")
#print(f"1st occurence of {query} in array {arr} is: {last_occur(arr,query)}")

