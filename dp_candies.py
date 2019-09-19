from operator import add

def candies(n, arr):
    incr = [0]*n
    incr[0] = 1
    for i in range(1,n):
        if arr[i-1] < arr[i]:
            incr[i] = incr[i-1] + 1
        else:
            incr[i] = 1
    dcr = [0]*n
    dcr[-1] = 1
    for i in range(n-2, -1, -1):
        if arr[i+1] < arr[i]:
            dcr[i] = dcr[i+1] + 1
        else:
            dcr[i] = 1
    return sum(list(map(max, incr, dcr)))

val = candies(10, [2, 4, 2, 6, 1, 7, 8, 9, 2, 1])
print(val)
