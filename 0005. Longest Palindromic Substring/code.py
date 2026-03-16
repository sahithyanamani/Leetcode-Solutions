class Solution:
    def longestPalindrome(self, s: str) -> str:
        # ---------------------------------------------------------
        # 1️⃣ Brute Force
        # Check every substring and verify if it is a palindrome
        # ---------------------------------------------------------
        '''
        res, maxlen = "", 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                l, r = i, j
                currlen = j - i + 1

                while l < r and s[l] == s[r]:
                    l += 1
                    r -= 1

                if l >= r and currlen > maxlen:
                    res = s[i:j+1]
                    maxlen = currlen

        return res

        # ⏱ Time Complexity: O(n^3)
        # - O(n^2) substrings
        # - O(n) to check palindrome
        #
        # 🧠 Space Complexity: O(1)
        '''

        # ---------------------------------------------------------
        # 2️⃣ Two Pointers / Expand Around Center
        # For each index, expand for:
        # - odd length palindrome  (center = i)
        # - even length palindrome (center = i, i+1)
        # ---------------------------------------------------------
        res, maxlen = "", 0

        for i in range(len(s)):

            # odd-length palindrome
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > maxlen:
                    res = s[l:r+1]
                    maxlen = r - l + 1
                l -= 1
                r += 1

            # even-length palindrome
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > maxlen:
                    res = s[l:r+1]
                    maxlen = r - l + 1
                l -= 1
                r += 1

        return res


# ---------------------------------------------------------
# 🧩 Explanation:
# - A palindrome mirrors around its center.
# - Every palindrome has either:
#   1️⃣ one center character   → odd length
#   2️⃣ two center characters  → even length
# - Expand outward while characters match.
# - Track the longest palindrome found.

# Example:
# s = "babad"
# centers:
# "bab" and "aba" are palindromes
# answer can be either "bab" or "aba"

# ---------------------------------------------------------
# ⏱ Time Complexity (Two Pointers): O(n^2)
# - n centers
# - each expansion can take O(n)

# 🧠 Space Complexity: O(1)
# - only pointers and variables used
# ---------------------------------------------------------
