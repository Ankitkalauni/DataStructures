def find_triplet(a,n):
    for i in range(len(a)): #will run from 0 to n-1
        p = i+1
        j = p+1
        while(j <= len(a)-1):
            if (a[i] + a[p] + a[j]) == n:
                print(a[i], a[p], a[j])
            p+=1
            j+=1

if __name__ == '__main__':
    find_triplet([0,1,2,3,4,5,6,7,8,9,10],n = 10)
