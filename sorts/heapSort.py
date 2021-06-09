arr = [9,8,7,55,5,54,2,1,1]

#heaps: tree based data structure - complete binary tree. A complete binary tree is one where
#all but potentially the lowest level of the tree is completely filled

 #heap sort - O(nlogn)

def maxHeapify(arr, size, index):
    largest = index
    left = 2*index+1
    right = 2*index+2

    if left < size and arr[largest] < arr[left]:
        largest = left
    if right < size and arr[largest] < arr[right]:
        largest = right
    
    if largest != index: #if we were not at the largest number but now we are, we can switch the two
        arr[index], arr[largest] = arr[largest], arr[index]
        maxHeapify(arr, size, largest)
        
def heapSort(arr):
    for i in range(int(len(arr)/2)-1, -1, -1): #build the heap
        maxHeapify(arr, len(arr), i)
        
    for i in range(len(arr)-1, 0, -1): #extract elements
        arr[i], arr[0] = arr[0], arr[i]
        maxHeapify(arr, i, 0)
        
heapSort(arr)
print(arr)