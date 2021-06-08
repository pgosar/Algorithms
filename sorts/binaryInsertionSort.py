#binary insertion sort

arr = [9,8,7,55,5,54,2,1,1]
 
def binarySearch(arr, val, start, end):
    if start == end:
        if arr[start] > val: #when we find the first element, if element to be sorted is smaller than first element we return the first index
            return start
        else:
            return start+1
    if start > end: #if end becomes too small because of mid-1 in line 30
        return start

    mid = (start+end)//2
    if arr[mid] < val:
        return binarySearch(arr, val, mid+1, end)
    elif arr[mid] > val:
        return binarySearch(arr, val, start, mid-1)
    else:
        return mid
 
def binaryInsertionSort(arr):
    for i in range(1, len(arr)):
        j=i-1
        val = arr[i]
        temp = binarySearch(arr, val, 0, i-1)
        while j >= temp: #while j is larger than the end index that the current element needs to go into, we traverse to the left and swap
            arr[j+1] = arr[j]
            j-=1
            arr[j+1] = val

binaryInsertionSort(arr)
print(arr)
