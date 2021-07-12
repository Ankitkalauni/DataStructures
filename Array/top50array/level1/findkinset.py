'''
Given an array arr[] and size of array is n and one another key x, 
and give you a segment size k. The task is to find that the key x 
present in every segment of size k in arr[].
Examples: 

Input : 
arr[] = { 3, 5, 2, 4, 9, 3, 1, 7, 3, 11, 12, 3} 
x = 3 
k = 3 
Output : Yes 
'''

def findxinkset(arr,x,k):
    n = len(arr)
    i = 0
    while (i<n):
        j = 0
        while (j<k):
            if (arr[i+j] == x):
                break
            j+=1
            if (j==k):
                return False
        i+=k
    if i==n:
        return True
    
    j = i-k
    
    while j<n:
        if arr[j] == x:
            break
        j+=1
    if j==n:
        return False
    return True

 
    i = 0
    while i < n :
 
        j = 0
         
        # Search x in segment
        # starting from index i
        while j < k :
             
            if arr[i + j] == x :
                break
             
            j += 1
 
        # If loop didn't break
        if j == k :
            return False
 
        i += k
         
    # If n is a multiple of k    
    if i == n :
        return True
 
    j = i - k
     
    # Check in last segment if n
    # is not multiple of k.
    while j < n :
        if arr[j] == x :
            break
 
        j += 1
 
    if j == n :
        return False
 
    return True
arr = [3, 5, 2, 4, 9, 3, 1, 7, 3, 11, 12, 3]
findxinkset(arr, x=2, k=3)
