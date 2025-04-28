mod = (10**9)+7
def countPartitions(n: int, d: int, arr: List[int]) -> int:
    total_sum = sum(arr)
    if (total_sum-d)%2!=0 or (total_sum-d)<0:
        return 0
    sum_ = (total_sum-d)//2
    prev = [0]*(sum_+1)
    prev[0] = 1
    
    for i in range(n):
        cur = [0]*(sum_+1)
        cur[0] = 1
        for j in range(sum_+1):
            not_take = prev[j]
            take = 0
            if arr[i]<=j:
                take = prev[j-arr[i]]
            cur[j] = (not_take+take)%mod

        prev = cur

    return prev[sum_]