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
