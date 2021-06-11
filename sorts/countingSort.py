arr = [9,8,7,55,5,54,2,1,1]

def countingSort(arr):
    counter = []
    ans = []
    for i in range(max(arr)-min(arr)+1): #filling lists with 0
        counter.append(0)
    
    for i in range(len(arr)):
        ans.append(0)
    
    for i in range(len(arr)): #counting occurences of each number
        counter[arr[i]-min(arr)] +=1
    
    for i in range(1, len(counter)): #now contains position
        counter[i] += counter[i-1]
    
    for i in range(len(arr)-1,-1,-1): #creating output
        ans[counter[arr[i]-min(arr)]-1] = arr[i]
        counter[arr[i]-min(arr)] -= 1
    
    return ans

print(countingSort(arr))