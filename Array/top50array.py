#leetcode

#1
'''
Given a binary array nums, return the maximum number of consecutive 1's in the array.
'''
nums = [1,1,0,1,1,1,1]

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        # count = 0
        # length = 0
        # for num in nums:
        #     if num == 1:
        #         length += 1
        #     else:
        #         count = max(length, count)
        #         count = 0
        # return max(count, length)
        countt = []
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count+=1
            elif nums[i] == 0:
                countt.append(count)
                count = 0
        if count != 0:
            countt.append(count)
        return max(countt)

            
sett = Solution()
sett.findMaxConsecutiveOnes(nums)

'''
Find Numbers with Even Number of Digits
'''
nums = [555,901,482,1771]

class Solution:
    def findNumbers(self, nums):
        countt = []
        count = 0
        for i in range(len(nums)):
            countt.append(len(str(nums[i])))
            
        for j in countt:
            if j%2==0:
                count+=1
        return count
            
sett = Solution()
sett.findNumbers(nums)

'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
'''

class Solution:
    def sortedSquares(self, numbs):
        n = len(numbs)
        for i in range(n):
            numbs[i] = numbs[i] * numbs[i]
        return sorted(numbs)
    
sol = Solution()
nums = [-4,-1,0,3,10]
sol.sortedSquares(nums)


'''
Median of Two Sorted Arrays
'''

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        '''
        merged_array = nums1 + nums2
        merged_array= sorted(merged_array)
        length= len(merged_array)
        if length%2 == 0:
            print("yes")
            median =  (merged_array[(length//2) -1] + merged_array[(length//2) ]) / 2
        else :
            median = merged_array[length//2]
            
        return median
        '''

        nums1+=nums2
        nums1.sort()
        n = len(nums1)
        mid = n/2
        if n%2==0:
            mid = int(mid)
            return (nums1[mid] + nums1[mid-1])/2
        else:
            return nums1[int(mid)]

        
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
  


# =============================================================================
# #GFG top 50 array coding problems
# 
# =============================================================================
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


'''
Range and Coefficient of range of Array

Range = Max – Min
Coefficient of Range = (Max – Min) / (Max + Min)
'''                
def coeflist(arr):
    maxx = max(arr)
    minn = min(arr)
    
    rangeis = maxx-minn
    cof = (maxx-minn)/(maxx+minn)
    
    print('Range:', rangeis,'\n','Coefficient of Range:', cof)


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
    
    

   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
