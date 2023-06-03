'''
If you read the code carefully, you will understand this algorithum easily
Time complexity: O(n*n). This algorithum sort the number from smaller to larger
if we change just one condition then this will sort the numbers from larger
to smaller.For this we need to convert
if(L[j]>L[j+1]): to if(L[j]<L[j+1]):
'''
def bubble_sort(L):
    n = len(L)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if(L[j]>L[j+1]):
                L[j],L[j+1]=L[j+1],L[j]

    return L

L = [3,1,7,6,2]
print(bubble_sort(L))