def shiftZero(arr1):
    i = 0
    while i < len(arr1)-1:
        temp = i + 1
        while temp < len(arr1):

            if arr1[i] == 0 and arr1[temp] != 0: #if current item is zero and next item is not zero
                arr1[temp], arr1[i] = arr1[i], arr1[temp] #swap

            elif arr1[i] == 0 and arr1[temp] == 0 and temp < len(arr1): #if next item is zero take one step
                temp +=1

            else:
                break

        i +=1


if __name__ == '__main__':
    arr1 = [2,3,0,6,0,5,8]

    shiftZero(arr1)
    for i in arr1:
        print(i, end = ' ')
