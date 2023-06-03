#Given an array of sorted integers, find two numbers such that they add up to a target number

def fun(L,x):
    i = 0
    j = len(L)-1

    while i<j:
        if(L[i]+L[j]==x):
            print(i,j)
            break

        elif (L[i]+L[j]<x):
            i+=1
        else:
            j-=1

    return -1

L = [2,4,5,7,11,15]
x = 12
fun(L,x)