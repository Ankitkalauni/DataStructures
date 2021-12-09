def find_pair(a,n):
    for i in range(len(a)): #will run from 0 to n-1
        temp = a[i] #get the current iter value to compare for pair

        j = i+1
        while(j <= len(a)-1):
            if (a[i] + a[j]) == n:
                print(a[i], a[j])
            j+=1


if __name__ == '__main__':
    find_pair([0,1,2,3,4,5,6,7,8,9,10],n = 10)
