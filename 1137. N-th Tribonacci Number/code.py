
class Solution:
    def tribonacci(self, n: int) -> int:

        t = [0, 1, 1]
        # ✅ Base values of Tribonacci sequence
        # T0 = 0
        # T1 = 1
        # T2 = 1

        # If n is within base cases
        if n < 3:
            return t[n]

        # ---------------------------------------------------------
        # Compute Tribonacci iteratively
        # Tn = Tn-1 + Tn-2 + Tn-3
        # ---------------------------------------------------------
        for i in range(3, n + 1):
            t[0], t[1], t[2] = t[1], t[2], sum(t)
            # shift values forward
            # new values represent next tribonacci number

        return t[2]   # final Tribonacci number


# ---------------------------------------------------------
# 🧩 Explanation:
# Tribonacci sequence extends Fibonacci:
#
# Tn = Tn-1 + Tn-2 + Tn-3
#
# Example:
# n = 5
# sequence:
# 0,1,1,2,4,7

# ---------------------------------------------------------
# ⏱ TIME COMPLEXITY (TC):
# O(n)
# - single loop from 3 → n

# 🧠 SPACE COMPLEXITY (SC):
# O(1)
# - only storing last three values
# ---------------------------------------------------------

