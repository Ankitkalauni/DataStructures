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
        
'''
4.4 Counting Sort
'''    
def countsort(arr):
    output = [0 for i in range(len(arr))]
    
    count = [0 for i in range(max(arr)+1)]
    
    for i in arr:
        count[i] += 1
    
    for i in range(len(count)-1):
        count[i+1] = count[i]+count[i+1]
    
    for i in range(len(arr)):
        output[count[arr[i]]-1] = arr[i]
        count[arr[i]]-=1
    

'''
4.5 radix sort(uses counting sort)

'''
def countsort(arr,exp1):
    n = len(arr)
    
    count = [0] *10
    
    output = [0]*n
    
    for i in range(n):
        index = arr[i] / exp1
        count[int(index%10)]+=1
        
    for i in range(1,10):
        count[i]+=count[i-1]
    
    i = n-1
    while i >=0:
        index = arr[i]/exp1
        output[count[int(index%10)]-1] = arr[i]
        count[int(index%10)]-=1
        i-=1
    
    i=0
    for i in range(n):
        arr[i] = output[i]
    
def radixsort(arr):
    maxx = max(arr)
    
    exp = 1
    while maxx/exp >0:
        countsort(arr, exp)
        exp=exp*10
    return arr

'''
5.6 insertion sort
'''

def insertionsort(arr):
    n = len(arr)
    
    
    for i in range(1,n):
        k = arr[i]    
        j = i-1
        
        while j>=0 and k <arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = k
    return arr
