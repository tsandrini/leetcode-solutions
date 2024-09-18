#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        sign = ''
        start = 0

        if s[0] in ["-", "+"]:
            sign = s[0]
            start = 1

            while start < len(s) and s[start] == "0":
                start += 1

        end = start
        while end < len(s) and s[end].isdigit():
            end += 1

        out = int(sign + s[start:end]) if s[start:end] else 0

        return max(min((out), 2**31 - 1), -2**31)

# @lc code=end
