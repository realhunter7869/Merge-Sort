def mergeSort(lst):
    if len(lst) > 1:
        mid = len(lst)//2
        L = lst[:mid]
        R = lst[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                lst[k] = L[i]
                i += 1
            else:
                lst[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            lst[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            lst[k] = R[j]
            j += 1
            k += 1
 
 
def printList(lst):
    for i in range(len(lst)):
        print(lst[i], end=" ")
    print()
 
lst = [12, 11, 13, 5, 6, 7]
print("Given list is", end="\n")
printList(lst)
mergeSort(lst)
print("Sorted list is: ", end="\n")
printList(lst)