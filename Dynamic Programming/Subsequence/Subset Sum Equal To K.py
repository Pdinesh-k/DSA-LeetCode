def subsetSumToK(n, k, arr):
    prev = [False]*(k+1)
    curr = [False]*(k+1)
    prev[0] = 1
    curr[0] = 1
    if arr[0]<=k:
        prev[arr[0]] = 1

    for i in range(1,n):
        for target in range(1,k+1):
            not_take = prev[target]
            take = False
            if arr[i]<=target:
                take = prev[target-arr[i]]
            curr[target] = take or not_take
        prev = curr[:]

    return prev[k]