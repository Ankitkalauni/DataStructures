'''
Find the frequency of a number in an array
'''

def frequency(arr,x):
    count = {}
    
    for i in range(len(arr)):
        if arr[i] in count:
            count[arr[i]]+=1
        else:
            count[arr[i]]=1
    return count.get(x)


arr = [1, 3, 2, 4, 2, 1]

frequency(arr, 2)