# Leetcode 91

def countDecodingDP(digits, n):
    dp = [0] * (n + 1)

    dp[0] = 1
    if digits[0] == '0':
        dp[1] = 0
    else:
        dp[1] = 1

    for i in range(2, n + 1):
        currentDigit = int(digits[i-1:i]) # Taking out one digit
        previousCurrentDigits = int(digits[i - 2:i]) #Taking out the two digits: current and immediate previous

        if currentDigit >= 1:
            dp[i] += dp[i-1]
        if previousCurrentDigits >= 10 and previousCurrentDigits <= 26:
            dp[i] += dp[i-2]

    return dp[n]

digits = "0";
n = len(digits);
print("Count is",
      countDecodingDP(digits, n));
