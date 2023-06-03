def findMedian(arr):
    n = len(arr)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
    left = 0
    right = len(arr)
    mid = (left+right)//2
    return arr[mid]

arr = [5,3,1,2,4]
print(findMedian(arr))