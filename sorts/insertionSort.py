arr = [9,8,7,55,5,54,2,1,1]

def insertionSort(arr):
    for i in range(1, len(arr)):
        temp=arr[i]
        j=i-1
        while j>=0 and temp < arr[j]:
            arr[j+1] = arr[j]
            j-=1
            arr[j+1]=temp

insertionSort(arr)
print(arr)
