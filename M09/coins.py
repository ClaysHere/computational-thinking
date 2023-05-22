def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    if dp[amount] == float('inf'):
        return -1
    else:
        return dp[amount]

n = int(input())
coins = list(map(int, input().split()))
amount = int(input())

print(coin_change(coins, amount))

# Kompleksitas O(n * amount)
