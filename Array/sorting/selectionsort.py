a = [69,4,8,0,3,1,2]

def selection(a): # O(n^2) good for short list

    for i in range(len(a)-1):
        minint = i

        for j in range(i+1,len(a)):
            if a[j] < a[minint]:
                minint = j

        a[i],a[minint] = a[minint], a[i]

    return a


temp = selection(a)

for i in temp:
    print(i)