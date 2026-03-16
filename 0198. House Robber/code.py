class Solution:
    def rob(self, nums: List[int]) -> int:
        # =========================================================
        # HOUSE ROBBER PROBLEM – 3 APPROACHES
        # =========================================================

        # ---------------------------------------------------------
        # 1️⃣ Recursion (Brute Force)
        # ---------------------------------------------------------
        '''
        n = len(nums)

        def helper(i):
            if i == 0:
                return nums[0]                 # only one house
            if i == 1:
                return max(nums[0], nums[1])   # choose best of first two houses

            # choice:
            # rob current house + skip previous
            # OR skip current house
            return max(nums[i] + helper(i-2), helper(i-1))

        return helper(n-1)


        ⏱ Time Complexity (TC): O(2^n)
        - Each call branches into two recursive calls.

        🧠 Space Complexity (SC): O(n)
        - Recursion call stack depth.
        '''


        # ---------------------------------------------------------
        # 2️⃣ Top-Down Dynamic Programming (Memoization)
        # ---------------------------------------------------------
        '''
        n = len(nums)

        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        memo = {0: nums[0], 1: max(nums[0], nums[1])}

        def helper(i):
            if i in memo:
                return memo[i]                 # reuse previously computed result

            memo[i] = max(nums[i] + helper(i-2), helper(i-1))
            return memo[i]

        return helper(n-1)


        ⏱ Time Complexity (TC): O(n)
        - Each index solved once due to memoization.

        🧠 Space Complexity (SC): O(n)
        - Memo dictionary + recursion stack.
        '''


        # ---------------------------------------------------------
        # 3️⃣ Bottom-Up DP (Tabulation with Space Optimization)
        # ---------------------------------------------------------

        n = len(nums)

        if n == 1:
            return nums[0]

        if n == 2:
            return max(nums[0], nums[1])

        prev = nums[0]                         # dp[i-2]
        curr = max(nums[0], nums[1])           # dp[i-1]

        for i in range(2, n):
            prev, curr = curr, max(nums[i] + prev, curr)
            # rob current house → nums[i] + prev
            # skip current house → curr

        return curr


        # ---------------------------------------------------------
        # 🧩 Explanation
        #
        # House Robber constraint:
        # cannot rob two adjacent houses.
        #
        # Recurrence:
        # dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        #
        # Example:
        # nums = [2,7,9,3,1]
        #
        # dp values:
        # 2,7,11,11,12
        #
        # answer = 12

        # ---------------------------------------------------------
        # ⏱ Time Complexity (TC): O(n)
        # - Single pass through array.

        # 🧠 Space Complexity (SC): O(1)
        # - Only two variables used.
        # ---------------------------------------------------------
