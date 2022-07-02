
def insertionsort(arr, n):
    for indx, i in enumerate(range(1,n)):
        temp = arr[i]
        j = i-1
        while j >= 0:
            if (arr[j] > temp):
                arr[j+1] = arr[j]
            else:
                break
            j -=1
        
        arr[j+1] = temp

    return arr

if __name__ == "__main__":
    arr = [10,3,7,4,5,9,2]
    n = 7

    sorted_arr = insertionsort(arr, n)

    print(sorted_arr)
