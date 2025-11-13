Initialize dp[0] = True

For each num in nums:
    For s = target → num:
        If dp[s - num] is True:
            dp[s] = True

Return dp[target]
