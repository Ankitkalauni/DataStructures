import array

arr = array.array('i',[1,2,3])

print('array: ', end = ' ')
for i in range(0,len(arr)):
    print(arr[i], end =  ' ')
    
arr.append(4)

# printing appended array
print("The appended array is : ", end="")
for i in range (0, 4):
    print (arr[i], end=" ")
    
# inserts 5 at 2nd position
arr.insert(2, 5)

print ("The array after insertion is : ", end="")
for i in range (0, 5):
    print (arr[i], end=" ")

# using pop() to remove element at 2nd position
print ("The popped element is : ",end="")
print (arr.pop(2))

# printing array after popping
print ("The array after popping is : ",end="")
for i in range (0,4):
    print (arr[i],end=" ")
    
# using remove() to remove 1st occurrence of 1
arr.remove(1)
 
# printing array after removing
print ("The array after removing is : ",end="")
for i in range (0,3):
    print (arr[i],end=" ")

# using index() to print index of 1st occurrenece of 2
print ("The index of 1st occurrence of 2 is : ",end="")
print (arr.index(2))
 
#using reverse() to reverse the array
arr.reverse()
 
# printing array after reversing
print ("The array after reversing is : ",end="")
for i in range (0,6):
    print (arr[i],end=" ")
    
