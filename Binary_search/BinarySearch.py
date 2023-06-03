'''
In this case, the list should be sorted(smaller to larger) and unique.
First we need to find the middle value, if this is the same as main value then return middle value, if the main value is not equal to the middle value and the main value is greater then middle value then left value = mid+1 otherwise right value = mid-1, In the initial phase, left value is 0 and the right value is len(L)-1 
'''
def binary_search(L,x):
    left=0
    right=len(L)-1

    while left<=right:
        mid = (left+right)//2 #integer division

        if(L[mid]==x):
            return mid
        if(L[mid]<x):
            left = mid+1
        else:
            right = mid-1

    return -1

#Index:0,1,2,3,4,5,6
L =   [2,3,4,6,7,9,13]
x = 15
print(binary_search(L,x))
