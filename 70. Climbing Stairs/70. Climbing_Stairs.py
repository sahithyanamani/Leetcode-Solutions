class Solution:
    def climbStairs(self, n: int) -> int:

        one, two = 1, 1
        # ✅ one = ways to reach current step
        # ✅ two = ways to reach previous step
        # Start from base cases:
        # step 1 → 1 way
        # step 0 → 1 way

        for i in range(n - 1):

            temp = one          # store current value
            one = one + two     # ways to reach next step
            two = temp          # shift previous value

        return one              # total ways to reach step n


# ---------------------------------------------------------
# 🧩 Explanation:
# At step i:
# ways[i] = ways[i-1] + ways[i-2]
#
# Because:
# - last move could be 1 step
# - or 2 steps
#
# This is Fibonacci sequence.

# Example:
# n = 5
# ways → 1,2,3,5,8

# ---------------------------------------------------------
# ⏱ TIME COMPLEXITY (TC):
# O(n)
# - single loop over steps

# 🧠 SPACE COMPLEXITY (SC):
# O(1)
# - only two variables used
# ---------------------------------------------------------
