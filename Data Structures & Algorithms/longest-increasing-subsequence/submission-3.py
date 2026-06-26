class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0 for i in nums]
        counter = 0
        for i in range(len(nums)):

            no = nums[i]
            j = i - 1
            lowest = no
            
            while j >= 0:
                counter = nums[j]
                if counter < no and lowest==no:
                    lowest = counter
                    flag = 1
                    dp[i] += dp[j]
                elif counter > lowest and counter < no:
                    dp[i] = max(dp[j], dp[i])
                    lowest = counter
                j -= 1
            dp[i] += 1
        print(dp)
        return max(dp)

