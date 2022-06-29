def bubblesort(a,n):
    count = 1
    while count < n:
        for i in range(0,n-count):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
            else:
                pass
        count +=1

    return a

if __name__ == '__main__':
    a = [6,7,1,9,2]
    n = len(a)

    temp = bubblesort(a,n)

    print(temp)
