'''
find the peek index of the mountain array in python.
'''

def peek(arr, size):

    start = 0
    end = size - 1

    while (start < end):
        mid = start + (end - start) // 2

        if arr[mid] < arr[mid + 1]:
            start = mid + 1
        else:
            end = mid

    return mid


if __name__ == '__main__':
    arr = [3,4,5,1]
    size = len(arr)

    print(peek(arr, size))
