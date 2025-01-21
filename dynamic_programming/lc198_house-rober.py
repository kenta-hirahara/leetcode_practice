def rob(nums: list[int]) -> int:
    match len(nums):
        case 0: return 0
        case 1: return nums[0]
        case 2: return max(nums)

    dp = [0 for _ in nums]
    for i, num in enumerate(nums):
        if i == 0:
            dp[i] = num
        if i == 1:
            dp[i] = max(dp[0], num)
        dp[i] = max(dp[i-2] + num, dp[i-1])
    return dp[-1]
        
print(rob([1,2,3,1]))
print(rob([2,7,9,3,1]))
