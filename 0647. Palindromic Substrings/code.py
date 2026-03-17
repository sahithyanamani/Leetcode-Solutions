class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        # ✅ Total count of palindromic substrings

        for i in range(len(s)):
            # -----------------------------------------------------
            # Count odd-length palindromes (center at i)
            # Example: "aba"
            # -----------------------------------------------------
            res += self.countpalindrome(s, i, i)

            # -----------------------------------------------------
            # Count even-length palindromes (center at i, i+1)
            # Example: "abba"
            # -----------------------------------------------------
            res += self.countpalindrome(s, i, i + 1)

        return res

    def countpalindrome(self, s, l, r):
        res = 0

        # ---------------------------------------------------------
        # Expand around center while characters match
        # Each successful expansion = one palindrome
        # ---------------------------------------------------------
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1          # ✅ found one palindrome
            l -= 1
            r += 1

        return res


# ---------------------------------------------------------
# 🧩 Explanation:
# Every palindrome can be expanded from its center.
#
# For each index:
# 1️⃣ Odd length → center at i
# 2️⃣ Even length → center between i and i+1
#
# Example:
# s = "aaa"
#
# Palindromes:
# "a", "a", "a", "aa", "aa", "aaa" → total = 6

# ---------------------------------------------------------
# ⏱ Time Complexity (TC): O(n^2)
# - n centers
# - each expansion takes up to O(n)

# 🧠 Space Complexity (SC): O(1)
# - no extra space used
# ---------------------------------------------------------
