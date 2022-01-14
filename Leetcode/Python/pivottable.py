'''find the pivot index in the given array'''

def pivot(arr, size):
    start = 0
    end = size - 1

    while(start < end):
        mid = start + (end - start) // 2

        if arr[mid] >= arr[0]:
            start = mid + 1

        else:
            end = mid

    return start

def findk(arr, indx, key):
    size = len(arr)

    if key >= arr[0]:
        start = 0
        end = indx - 1
    else:
        start = indx
        end = size - 1

    while(start <= end):
        mid = start + (end - start) // 2

        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return -1


if __name__ == '__main__':
    arr = [7,9,1,2,3]
    size = len(arr)

    indx = pivot(arr, size)

    print(findk(arr, indx, 11))



