def longest_palindrome(s):
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i + l - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    return dp[0][n-1]

t = int(input())
for i in range(t):
    s = input()
    print(longest_palindrome(s))

# Komppleksitas O(n^2)