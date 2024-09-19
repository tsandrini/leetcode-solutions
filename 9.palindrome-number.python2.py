# @leet start
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        if (len(x) % 2) == 0:
            start = (len(x) // 2) - 1
            end = len(x) // 2
        else:
            start = (len(x) // 2) - 1
            end = (len(x) // 2) + 1

        i = 0
        while i <= start:
            if x[start - i] != x[end + i]:
                return False
            i += 1

        return True
        
# @leet end
