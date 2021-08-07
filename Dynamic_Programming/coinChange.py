'''

You are given an integer array coins representing coins of different denominations 
and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount 
of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

'''


# Coin charge, Leet Code 322

def coinChange(coins, amount):
    coins = sorted(coins)
    print(coins)
    dp = [amount + 1] * (amount + 1)  # You can choose any max number, float("inf")
    dp[0] = 0  # Ex: dp[5] represents the min number of coins for making up 5 cents
    for i in range(1, amount + 1):  # We need to return dp[amount]
        for j in range(len(coins)):
            if coins[j] <= i:
                dp[i] = min(dp[i], 1 + dp[i - coins[j]])  # Adding 1 because we are using the current coin
            else:
                break

    print(dp)
    if dp[amount] == amount + 1:
        return -1
    else:
        return dp[amount]


print(coinChange([5, 2, 1], 11))
# Time = O(nlogn) for sorting
# Space = O(n), where n is the amountt
