arr = [9,8,7,55,5,54,2,1,1]

#The maximum value of an integer is 2147483647. It has 10 digits
#I will use this to make writing the code a bit simpler
#note that the counting sort algorithm needs to change as well because
#radix sort works off of individual digits

def countingSort(arr, digit):
    counter = []
    ans = []
    for i in range(10): #filling lists with 0
        counter.append(0)
    
    for i in range(len(arr)):
        ans.append(0)

    for i in range(len(arr)):
        num = arr[i]/digit
        counter[int(num%10)] +=1
    
    for i in range(1,10):
        counter[i] += counter[i-1]
    
    i = len(arr)-1
    while i >= 0:
        num = arr[i]/digit
        ans[counter[int(num%10)]-1] = arr[i]
        counter[int(num%10)] -=1
        i -=1
        
    for i in range(len(arr)):
        arr[i] = ans[i]
    
def radixSort(arr):
    digit = 1
    
    while max(arr)/digit >0:
        countingSort(arr,digit)
        digit *=10

radixSort(arr)
print(arr)