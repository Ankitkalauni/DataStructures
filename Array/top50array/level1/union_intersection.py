'''
Union and Intersection of two sorted arrays
'''

def union(arr1,arr2):
    n = arr1[-1]
    m = arr2[-1]

    union = []
    maxx = 0

    if n>m:
        maxx = n
    else:
        maxx = m
        
    count = [0] *(maxx+1)
    union.append(arr1[0])
    count[arr1[0]]+=1
    
    for i in range(1,len(arr1)):
        if arr1[i] != arr1[i-1]:
            union.append(arr1[i])
            count[arr1[i]]+=1
            
    for i in range(len(arr2)):
        if count[arr2[i]] == 0:
            union.append(arr2[i])
            count[arr2[i]]+=1
    return union
            
def intersection(arr1,arr2):
    n = len(arr1)
    m = len(arr2)
    
    i,j =0,0
    
    while i<n and j<m:
        if arr1[i] < arr2[j]:
            i+=1
        elif arr2[j]<arr1[i]:
            j+=1
        else:
            print(arr1[i])
            i+=1
            j+=1
    
 