def unique(a):
    ans = 0
    for i in range(len(a)):
        ans ^= a[i]
    return ans

if __name__ == '__main__':
    a=[1,2,3,3,2]
    unique(a)
