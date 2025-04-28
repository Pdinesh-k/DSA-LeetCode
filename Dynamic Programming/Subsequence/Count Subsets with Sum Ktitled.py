def findWays(arr, k):
        MOD = 10 ** 9 + 7
        n = len(arr)
        prev = [0]*(k+1)
        prev[0] = 1
        if arr[0]<=k:
            prev[arr[0]]=1

        for index in range(1,n):
            curr = [0] * (k + 1)
            curr[0] = 1
            for sum_ in range(1,k+1):
                not_take = prev[sum_]
                take = 0
                if arr[index]<=sum_:
                    take = prev[sum_-arr[index]]
                curr[sum_] = (take+not_take)%MOD
            prev = curr

        return prev[k]