"""Count repeated elements in a sorted array
arr = [2,4,10,10,10,18,20]"""
#O/P: 3

from duplicate import first_occur, last_occur

arr = [2,4,10,10,10,18,20]
query =10

f_occur = first_occur(arr,query)
l_occur = last_occur(arr,query)

count = l_occur - f_occur + 1
print(f"Count: {count}")