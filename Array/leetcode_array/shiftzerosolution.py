def shiftZero(arr):
    i = 0
    
    for j in range(len(arr)):
        if arr[j] != 0:
            arr[j], arr[i] = arr[i], arr[j]
            i +=1


if __name__ == '__main__':
    arr1 = [2,3,0,6,0,5,8]
    shiftZero(arr1)
    for i in arr1:
        print(i, end = ' ')
