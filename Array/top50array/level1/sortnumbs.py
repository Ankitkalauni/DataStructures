'''
5.Sort an array of 0s, 1s and 2s
'''
def sortnum(arr):
    low = 0
    high = len(arr) -1
    
    mid = 0
    
    while mid<=high:
        if arr[mid]==0:
            arr[low],arr[mid] = arr[mid],arr[low]
            low+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
            
        else:
            arr[high],arr[mid] = arr[mid],arr[high]
            high-=1
    return arr
