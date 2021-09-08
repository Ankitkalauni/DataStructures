def Split_rotate(array,k):
    first = array[:k]
    last = array[k:]
    join = last + first

    return join


arr = [12, 10, 5, 6, 52, 36]

new  = Split_rotate(arr,2)
