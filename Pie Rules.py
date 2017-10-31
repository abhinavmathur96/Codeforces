import sys
sys.setrecursionlimit(10**9)
n = input()
arr = map(int,raw_input().strip().split())
dp = [[0,0] for i in range(n)]
dp[n-1][1] = arr[i]
for i in range(n-2,-1,-1):
    dp[i][0] = min(dp[i+1][1],dp[i+1][0]+arr[i])
    dp[i][1] = max(dp[i+1][1],dp[i+1][0]+arr[i])
bob = max(dp[0][0],dp[0][1])
print sum(arr)-bob,bob
