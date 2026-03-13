class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        cost.append(0)
        # ✅ Add a "top" step with cost 0
        # So we can treat reaching the top like any other step

        # ---------------------------------------------------------
        # Dynamic Programming from the back
        # cost[i] becomes the minimum cost to reach the top from step i
        # ---------------------------------------------------------
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
            # From step i you can move to:
            # i+1 or i+2
            # so take the cheaper path

        # ---------------------------------------------------------
        # You can start from step 0 or step 1
        # Return the cheaper starting option
        # ---------------------------------------------------------
        return min(cost[0], cost[1])


# ---------------------------------------------------------
# 🧩 Explanation:
# Each step stores the minimum cost required to reach the top.
#
# Example:
# cost = [10,15,20]
#
# After DP:
# cost = [25,15,20,0]
#
# Answer = min(25,15) = 15

# ---------------------------------------------------------
# ⏱ TIME COMPLEXITY (TC):
# O(n)
# - Single backward pass through cost array

# 🧠 SPACE COMPLEXITY (SC):
# O(1)
# - In-place DP (no extra array used)
# ---------------------------------------------------------
