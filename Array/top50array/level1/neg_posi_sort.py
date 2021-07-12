'''
Move all negative numbers to beginning and positive to end 
with constant extra space
'''    
    
def rearrange(arr):
    n = len(arr)
    
    j = 0
    for i in range(0,n):
        if arr[i]<0:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j+=1
    return arr
