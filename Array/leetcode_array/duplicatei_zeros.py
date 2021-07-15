'''
Given a fixed length array arr of integers, duplicate each occurrence of zero
shifting the remaining elements to the right.
'''

def duplicateZeros(arr):
    """
    tmp = [0] * len(arr)
    j = 0
    i = 0
    # print(arr)
    while j < len(arr):
        # print(tmp, i, j)
        if arr[i] == 0 and j < len(arr) - 1:
            tmp[j] = 0
            tmp[j+1] = 0
            j += 2
        else:
            tmp[j] = arr[i]
            j += 1
        i += 1
    for i,v in enumerate(tmp):
        arr[i] = tmp[i]
    
    """
    n = len(arr) -1
    
    for i in range(n,-1,-1):
        if i==n:
            pass
        elif arr[i]==0:
            for p in range(n,i,-1):
                arr[p] = arr[p-1]
  
