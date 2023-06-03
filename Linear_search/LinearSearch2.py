'''
This is another procedure
'''
def linear_search(L,x):
    for i in range(len(L)):
        if(L[i]==x):
            return i
    
    return -1

L = [2,6,3,9,7,4,6,13]
x = 1
print(linear_search(L,x))
