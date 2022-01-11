'''Binary Search first and last occurance of the given key'''

def findleftkey(arr, size, key):
    start = 0
    end = size - 1 
    store = []
    while start <= end:
        mid = start + ((end -start) // 2)
    
        if arr[mid] == key: #if the key is mid
            store.append(mid) #store the index
            end = mid - 1

        if key < arr[mid]:
            end = mid - 1
 
        elif key > arr[mid]:
            start = mid + 1

    if store:
        return sorted(store)[0]

    return -1

def findrightkey(arr, size, key):
    start = 0
    end = size - 1 
    store = []
    while start <= end:
        mid = start + ((end -start) // 2)
    
        if arr[mid] == key:
            store.append(mid)
            start = mid + 1
        if key > arr[mid]:
            start = mid +1             
        elif key < arr[mid]:
            end = mid - 1

    if store:
        return sorted(store)[-1]

    return -1

def key_length(arr, size, key):
    min_val = findleftkey(arr, size, key)
    max_val = findrightkey(arr, size, key)

    return min_val, max_val

if __name__ == '__main__':
    print('started')
    arr = [0 ,0 ,1 ,1 ,2 ,2 ,2, 2]
    key = 2
    min_val, max_val = key_length(arr,len(arr), key)
    print(f'length of {key} is:',min_val, max_val)