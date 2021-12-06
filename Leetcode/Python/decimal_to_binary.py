def decimal_to_binary(n):
    store = 0
    i = 0
    while n != 0:

        bit = n&1
        store += bit * 10 ** i
        n = n >> 1
        i += 1

    return store

decimal_to_binary(5)