# =============================================================================
# Program to cyclically rotate an array by one
# 
# Following are steps. 
# 1) Store last element in a variable say x. 
# 2) Shift all elements one position ahead. 
# 3) Replace first element of array with x.
# =============================================================================

def cyclicrotation(arr):
    n= len(arr)
    x = arr[n-1]
    
    for i in range(n-1,0,-1):
        arr[i] = arr[i-1]
    arr[0] = x
    return arr

# =============================================================================
# Another approach:
# 
# We can use two pointers, say i and j which point to first and last 
#element of array respectively. As we know in cyclic rotation we will 
#bring last element to first and shift rest in forward direction, so start 
#waping arr[i] and arr[j] and keep j fixed and i moving towards j. 
#Repeat till i is not equal to j.
# 
# =============================================================================


def rotate(arr):
    n = len(arr)
    
    i = 0
    j= n-1
    
    while(i!=j):
        arr[i], arr[j] = arr[j], arr[i]
        i+=1
    return arr