# =============================================================================
# METHOD 1 (Using temp array) 
# 
# Input arr[] = [1, 2, 3, 4, 5, 6, 7], d = 2, n =7
# 1) Store the first d elements in a temp array
#    temp[] = [1, 2]
# 2) Shift rest of the arr[]
#    arr[] = [3, 4, 5, 6, 7, 6, 7]
# 3) Store back the d elements
#    arr[] = [3, 4, 5, 6, 7, 1, 2]
# =============================================================================
# =============================================================================
# 
# METHOD 2 (Rotate one by one)  
# 
# leftRotate(arr[], d, n)
# start
#   For i = 0 to i < d
#     Left rotate all elements of arr[] by one
# end
# =============================================================================

class arrayrotation():

    def rotationbyd(self,arr,d,n):
        for i in range(d):
            self.rotationleft(arr,n)    
            
    def rotationleft(self,arr,n):
        temp = arr[0]
        for i in range(n-1):
            arr[i] = arr[i + 1]
        arr[n-1] = temp

    def printArray(self,arr, size):
        for i in range(size):
            print ("% d"% arr[i], end =" ")
            
            
arr = [1, 2, 3, 4, 5, 6, 7]

rotation = arrayrotation()

rotation.rotationbyd(arr, 2, 7)
rotation.printArray(arr, 7)


# =============================================================================
# METHOD 3 (A Juggling Algorithm) 
# This is an extension of method 2. Instead of moving one by one, divide the array in different sets 
# where number of sets is equal to GCD of n and d and move the elements within sets. 
# If GCD is 1 as is for the above example array (n = 7 and d =2), then elements will be moved within one set only, we just start with temp = arr[0] and keep moving arr[I+d] to arr[I] and finally store temp at the right place.
# Here is an example for n =12 and d = 3. GCD is 3 and 
#  
# 
# Let arr[] be {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
# 
# a) Elements are first moved in first set – (See below 
#    diagram for this movement)
# 
# 
#           arr[] after this step --> {4 2 3 7 5 6 10 8 9 1 11 12}
# 
# b)    Then in second set.
#           arr[] after this step --> {4 5 3 7 8 6 10 11 9 1 2 12}
# 
# c)    Finally in third set.
#           arr[] after this step --> {4 5 6 7 8 9 10 11 12 1 2 3}
# =============================================================================

class juggling():
    def rotate(self,arr,d,n):
        d = d % n
        gcdd = self.gcd(d,n)
        for i in range(gcdd):
            temp = arr[i]
            j = i
            while 1:
                k = j + d
                if k >=n:
                    k = k-n
                if k == i:
                    break
                arr[j] = arr[k]
                j = k
            arr[j] = temp
            
    def printarray(self,arr,size):
        for p in range(size):
            print("% d" % arr[p], end = ' ')
            
        
    def gcd(self,a,b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)
        
arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
d = 2
jug = juggling()

jug.rotate(arr, d, n)
jug.printarray(arr, n)

