'''
Time complexity: O(n*n). This algorithum sort the number from smaller to larger
if we change just one condition then this will sort the numbers from larger
to smaller.For this we need to convert
if(L[j]<L[index_min]): to if(L[j]>L[index_min]):
''' 
def selection_sort(L):
    n = len(L)

    for i in range(0,n-1):
        index_min = i
        for j in range(i+1,n):
            if(L[j]<L[index_min]):
                index_min = j

        if index_min!=i:
            L[i],L[index_min]= L[index_min],L[i]
            
    return L

L = [6,1,4,9,2]
print(selection_sort(L))
