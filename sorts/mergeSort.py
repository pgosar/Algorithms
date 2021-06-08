arr = [9,8,7,55,5,54,2,1,1]

def mergeSort(arr):
    if len(arr) > 1:
        i=j=k=0
        mid = int(len(arr)/2)
        left = arr[:mid]
        right = arr[mid:]
        mergeSort(left)
        mergeSort(right)
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
            k+=1
        while i < len(left):
            arr[k] = left[i]
            i+=1
            k+=1
        while j < len(right):
            arr[k] = right[j]
            j+=1
            k+=1
"""
this code splits down arr until it reaches a length of 1
once it does that it looks at the first element in the left array, compares it to the first in the right, and adds the lesser of the two to arr
it does that until either i or j reaches the end of their list, and then adds on the remainder from either i or j, 
the remainder will always be the largest number and there will only be one at most, which happens when the original array has an odd length
"""
mergeSort(arr)
print(arr)
