# First attempt ->
# Solution based around expanding around center
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         N: int = len(s)
#         if N < 2:
#             return s
#         longest_str: str = s[1]
#         longest_len: int = 1

#         for i in range(N - 1):
#             buff: str = s[i]
#             j: int = 1
#             k: int = 1
#             c: str = s[i]
#             # first we check for repeating characters, ie
#             # aa, aaa, aaaaa, .....
#             while True:
#                 if i + k >= N or not (s[i + k] == c):
#                     break
#                 buff += c
#                 k += 1

#             # then we check for nontrivial palindromes, ie
#             # aba, abcba, abcdcba, (as well as abbba)
#             while True:
#                 if i - j < 0 or i + k >= N or not (s[i - j] == s[i + k]):
#                     break

#                 buff = s[i - j] + buff + s[i + k]
#                 j += 1
#                 k += 1

#             if (j + k - 1) > longest_len:
#                 longest_str = buff
#                 longest_len = j + k - 1

#         return longest_str


# DP approach -> this is somehow slower than my first attempt? wtf?
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         N: int = len(s)
#         if N < 2:
#             return s
#         longest_str: str = s[1]
#         longest_len: int = 1

#         dp = [[False for _ in range(N)] for _ in range(N)]

#         for i in range(N):
#             # f(0) case, the bootstrapping rule for the induction/recursion
#             dp[i][i] = True

#             for j in range(i):
#                 # The inductive/recursive step
#                 if (s[i] == s[j]) and (i - j <= 2 or dp[j + 1][i - 1]):
#                     dp[j][i] = True
#                     if i - j + 1 > longest_len:
#                         longest_str = s[j : i + 1]
#                         longest_len = i - j + 1

#         return longest_str


# Naive solution with string preprocessing
# somehow faster then DP??
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        s = "#" + "#".join(s) + "#"
        N: int = len(s)
        longest_str: str = s[1]
        longest_len: int = 1

        for i in range(1, N - 1):
            j: int = 1

            while i - j >= 0 and i + j < N and s[i - j] == s[i + j]:
                j += 1

            if (j - 1) > longest_len:
                longest_len = j - 1
                start = (i - longest_len) // 2
                longest_str = s[2 * start : (start + longest_len) * 2 + 1]

            # Optimalization -> skip if we cannot construct larger palindromes
            if longest_len >= (N - 1 - i):
                break

        return longest_str.replace("#", "")
