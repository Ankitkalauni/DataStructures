

def mergeSort(arr1,arr2,arr3):
    i,j = 0,0

    while (i < len(arr1) and (j < len(arr2))):
        if arr1[i] < arr2[j]:
            arr3.append(arr1[i])
            i+=1

        else:
            arr3.append(arr2[j])
            j+=1

    while (i < len(arr1)):
        arr3.append(arr1[i])
        i += 1

    while (j < len(arr2)):
        arr3.append(arr2[j])
        j += 1

if __name__ == "__main__":

    arr1=[1,3,5,7,9]
    arr2=[2,4,6,8]

    arr3 = []

    mergeSort(arr1,arr2,arr3)

    for i in range(len(arr3)):
        print(arr3[i], end = " ")
        