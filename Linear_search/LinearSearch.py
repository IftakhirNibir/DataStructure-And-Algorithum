'''
In Linear Search, we actually check values from the begining to the end 
sequentially. When find the value x in list L then return the index no of the list. Here Time Complexity is O(n) and Space complexity is O(1)
'''

def linear_search(L,x):
    n = len(L) #Total length 
    i = 0
    while i<n: #This condition will work untill i <= len(n)-1 so if len = 9 the highest i value will be 8
        if(L[i]==x):
            return i
        
        i+=1
        
    return -1


L = [2,6,3,9,7,4,6,13]
x = 2

print(linear_search(L,x))
