#top 50 array coding problems

#1
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



#2
'''
# Python3 program to find minimum
# (or maximum) element in an array

Time Complexity:O(n)
'''

def getMin(arr,n):
    ele = arr[0]
    for i in range(1,n):
        ele = min(ele,arr[i])
    return ele

def getMax(arr,n):
    ele = arr[0]
    for i in range(1,n):
        ele = max(ele,arr[i])
    return ele

arr = [12, 1234, 45, 67, 1]
n = len(arr)
print ("Minimum element of array:", getMin(arr, n))
print ("Maximum element of array:", getMax(arr, n))


#3
'''
Write a program to reverse an array or string
'''
#3.1 

def reversearr(arr):
    n = len(arr)
    start = 0
    end = n-1
    for i in range(0,n-1):
        arr[start], arr[end] = arr[end], arr[start]
        start+=1
        end-=1
        
    return arr


#3.2 recursive method

def reverse(arr,start,end):
    if start >= end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    reverse(arr,start+1,end-1)
    return arr


#3.3 python list slicing

def reverselist(arr):
    arr = arr[::-1]
    return arr

#4
'''
python program to sort an array in ascending order
'''
#4.1 selection sorting 
#O(n^2) as there are two nested loops.


def selectionsort(arr):
    n = len(arr)
    for i in range(n):
        indx = i
        for j in range(i+1,n):
            if arr[indx] > arr[j]:
               arr[indx], arr[j] = arr[j],arr[indx] 
    
    return arr

#4.2 bubble sorting

def bubblesort(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]

    return arr


#4.3 Merge sort

def mergesort(arr):
    if len(arr)>1:
        n = len(arr)
        
        mid = n//2
        
        L = arr[:mid]
        R = arr[mid:]
        
        mergesort(L)
        mergesort(R)
        
        i=j=k = 0
        while i<len(L) and  j <len(R):
            if L[i]<R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1
        
        while i<len(L):
            arr[k] = L[i]
            i+=1
            k+=1
        
        while j<len(R):
            arr[k] = R[j]
            j+=1
            k+=1
        
    return arr

arr = [12, 11, 13, 5, 6, 7]

mergesort(arr)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
