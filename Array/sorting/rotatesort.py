# code to check if array is shorted and rotated or not
def rotatesort(arr):
    count = 0
    n = len(arr)

    for i in range(1,n):
        if arr[i-1] > arr[i]:
            count +=1

    if arr[n-1] > arr[0]:
        count +=1

    return count <=1

if __name__ == "__main__":
    arr = [3,4,5,6,7,1,2]

    print(rotatesort(arr))