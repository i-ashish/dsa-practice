"""Array is sorted but ascending or descending not known"""

from ascending import ascending_element
from descending import descending_element

def agnostic(arr,query):

    if len(arr) > 1:
        if arr[0] < arr[1]:
            return ascending_element(arr,query)

        else: return descending_element(arr,query)

    elif len(arr) == 1:
        return arr[0]

    else: return -1


arr = [1,2,3,4,5,6,7,8,9,10]
print(agnostic(arr,2))

arr = [20,17,15,14,13,13,10,9,8,4]
print(agnostic(arr,4))