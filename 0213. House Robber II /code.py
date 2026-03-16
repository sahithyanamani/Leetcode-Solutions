class Solution:
    def rob(self, nums: List[int]) -> int:
        # ---------------------------------------------------------
        # House Robber II (Circular houses)
        # First and last house cannot both be robbed.
        # So solve two cases:
        # 1️⃣ Rob houses [1..n-1]
        # 2️⃣ Rob houses [0..n-2]
        # ---------------------------------------------------------

        if len(nums) == 1:
            return nums[0]  # only one house

        return max(self.helper(nums[1:]), self.helper(nums[:-1]))


    def helper(self, nums):
        prev, curr = 0, 0
        # prev → dp[i-2]
        # curr → dp[i-1]

        for i in nums:
            newrob = max(prev + i, curr)
            # rob current house → prev + value
            # skip house → curr

            prev, curr = curr, newrob

        return curr


# ---------------------------------------------------------
# 🧩 Explanation
#
# House Robber II:
# Houses are arranged in a circle.
# So first and last houses cannot both be robbed.
#
# Example:
# nums = [2,3,2]
#
# Case1: rob [3,2] → 3
# Case2: rob [2,3] → 3
#
# Answer = 3
#
# ---------------------------------------------------------
# ⏱ Time Complexity (TC):
# O(n)
# - helper runs twice over array

# 🧠 Space Complexity (SC):
# O(1)
# - only two variables used
# ---------------------------------------------------------
