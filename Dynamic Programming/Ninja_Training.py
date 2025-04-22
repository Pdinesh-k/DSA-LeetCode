def recursion(arr,day,last,dp):
    if day == 0:
        max_0 = float("-inf")
        for i in range(0,3):
            if i!=last:
                max_0 = max(arr[0][i],max_0)
        return max_0

    if dp[day][last]!=-1:
        return dp[day][last]

    max_profit = float("-inf")
    for i in range(0,3):
        if i!=last:
            curr = arr[day][i]+recursion(arr,day-1,i,dp)
            max_profit = max(curr,max_profit)
    dp[day][last] = max_profit
    return max_profit

def ninja_Training(n,arr,dp):
    day = n-1
    last = -1
    return recursion(arr,day,last,dp)

arr = [[18,11,19],[4,13,7],[1,8,13]]
dp = [[-1]*len(arr[0]) for _ in range(len(arr))]
print(ninja_Training(3,arr,dp))