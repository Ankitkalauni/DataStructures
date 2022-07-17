def addarray(arr1, arr2):
    arr3 = []

    i = len(arr1) - 1
    j = len(arr2) - 1

    carry = 0
    _sum = 0
    ans = 0


    while (i >=0 and j >= 0):
        _sum = arr1[i] + arr2[j] + carry

        carry = int(_sum / 10)
        ans = int(_sum % 10)

        arr3.insert(0,ans)

        i-=1
        j-=1

    while (i >=0):
        _sum = arr1[i] + carry
        carry = int(_sum / 10)
        ans = int(_sum % 10)

        arr3.insert(0,ans)

        i-=1

    while (j >=0):
        _sum = arr2[j] + carry
        carry = int(_sum / 10)
        ans = int(_sum % 10)

        arr3.insert(0,ans)

        j-=1

    while (carry != 0):
        sum = carry
        carry = int(_sum / 10)
        ans = int(_sum % 10)

        arr3.insert(0,ans)

    return arr3

if __name__ == "__main__":
    arr1 = [4,5]
    arr2 = [3,5,7,8]

    arr3 = addarray(arr1, arr2)

    for i in arr3:
        print(i, end= ' ')