def swap(a):
    i = 0
    ii = i+1

    while(i != len(a)):
        try:
            a[i],a[ii] = a[ii],a[i]
            i+=2
            ii+=2
        except:
            break

    return a


def better_swap(a):
    i = 0
    while(i+1<len(a)):
        a[i],a[i+1] = a[i+1], a[i]
        i+=2
    return a

if __name__ == '__main__':
    a = [1,4,6,7,9,6,3,68,0]
    better_swap(a)
