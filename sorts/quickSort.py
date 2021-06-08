arr = [9,8,7,55,5,54,2,1,1]

def partition(arr, left, right):
    index = left
    pivot = arr[left]
    while left < right:
        while left < len(arr) and arr[left] <= pivot: #left side of the array, iterates until it finds pivot
            left += 1

        while arr[right] > pivot: #right side of the array, iterates until it finds pivot
            right -= 1
        
        if right > left: 
            arr[left], arr[right] = arr[right], arr[left] #:D just learned about this method of swapping
     
    arr[right], arr[index] = arr[index], arr[right]
    return right #does the splitting

def quickSort(arr, left, right):
    if right > left:
        index = partition(arr, left, right)
        quickSort(arr, left, index-1)
        quickSort(arr, index+1, right)

quickSort(arr, 0, len(arr)-1)
print(arr)

#O(nlogn) - iterating through list is n, splitting it in  half with the recursions is logn