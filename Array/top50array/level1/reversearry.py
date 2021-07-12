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
