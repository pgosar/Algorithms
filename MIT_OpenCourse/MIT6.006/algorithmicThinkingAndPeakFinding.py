#find a peak in input if it exists
#input = [2,3,4,1,5,6,71,3,43,43,6,457,234,34,21325]

#this is the straightforward algorithm, how can we reduce time complexity?
input = [1,2,3,4,5,4,3,1]
def peakFinder(input):
    flag = False
    if input[len(input)-1] > input[len(input)-2]:
        print(input[len(input)-1])

    for i in range(len(input)-1):
        if input[i] > input[i+1] and input[i] > input[i-1]:
            print(input[i])
            flag = True
    if(not flag):
        print("no peak")

#time complexity:  O(n), space complexity O(n)

#using a binary search can reduce time complexity by letting us only search
#through half of the array 
arr = [1,2,3,4,5,65,4,43,4,3,2,1] #note that this will only find one peak
def binaryPeakFinder(arr, left, right):
    if left==right: #base case
        return left
    mid = int((left + right)/2)
    if arr[mid] > arr[mid+1]:
        return binaryPeakFinder(arr, left, mid) 
    else:
        return binaryPeakFinder(arr, mid+1, right)

print(arr[binaryPeakFinder(arr, 0, len(arr)-1)])

#time complexity: O(logn), space complexity O(n)

#2d version of peak finding  

#greedy ascent algorithm
arr = [[1,2,3,4],
       [8,7,6,5],
       [9,10,11,12],
       [16,15,14,13]]
rows = len(arr)
cols = len(arr[0])
def TwoDPeak(i, j):


    if(i > 0 and arr[i-1][j] > arr[i][j]):
        return TwoDPeak(i-1, j)

    elif(j > 0 and arr[i][j-1] > arr[i][j]):
        return TwoDPeak(i, j-1)

    elif(j < cols-1 and arr[i][j+1] > arr[i][j]):
        return TwoDPeak(i, j+1)

    elif(i < rows-1 and arr[i+1][j] > arr[i][j]):
        return TwoDPeak(i+1, j)

    else:
        return arr[i][j]

print(TwoDPeak(int(rows/2), int(cols/2)))
#time complexity O(n) best case, O(n*m) worst case