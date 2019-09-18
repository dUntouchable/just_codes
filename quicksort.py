a = [9, 8  , 4, 5, 32, 64, 2, 1, 0, 10,19, 27]

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    les, gre = [], []
    pivot = arr[-1]
    for i in range(len(arr)-1):
        if arr[i] <= pivot: les.append(arr[i])
        else: gre.append(arr[i])
    return quicksort(les) + [pivot] + quicksort(gre)

print(quicksort(a))
