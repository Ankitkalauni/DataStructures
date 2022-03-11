def ispossible(arr, n, m, mid):
    pagesum = 0
    studentaloc = 1
    

    for i in range(n):
        print(i, "inside ispossible loop")
        if ((pagesum + arr[i]) <= mid):
            pagesum += arr[i]
        else:
            studentaloc += 1
            if ((studentaloc > m)  or (arr[i] > mid)):
                print('returning false from ispossible')
                
                return 0

        pagesum = arr[i]
        
        if studentaloc > m:
            print('returning false from ispossible')
            return 0
        
    print('returning true from ispossible')
    return 1

def bookallocation(arr, n, m):
    #store sum of whole arr
    s = 0
    sum = 0

    for i in range(n):
        sum += arr[i]

    #end and mid value
    e = sum
    mid = (s + (e-s)) // 2
    ans = -1

    while (s<=e):
        print('inside main loop value - ',s,"--",e)
        if (ispossible(arr, n, m, mid)):
            print('got positive')
            ans = mid
            e = mid - 1
        
        else:
            print('got negative')
            s = mid + 1
        
        print('updating mid value -->', mid)
        mid = (s + (e - s)) // 2
    print('printing ans')
    return ans



if __name__ == "__main__":
    arr = [5,5,5,5,5]

    print(bookallocation(arr, len(arr), 2))
