# Trivial solution
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         N: int = len(s)

#         if N <= 1:
#             return N

#         max_len: int = 0
#         buff_str: str = ""
#         for i in range(N - 1):
#             buff_str = s[i]
#             for j in range(i + 1, N):
#                 char = s[j]
#                 if char in buff_str:
#                     max_len = max(max_len, len(buff_str))
#                     break
#                 else:
#                     buff_str += char
#             max_len = max(max_len, len(buff_str))

#         return max_len


# Trivial solution without len
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         N: int = len(s)
#         if N <= 1:
#             return N
#         max_len: int = 0
#         buff_str: str = ""
#         for i in range(N - 1):
#             buff_str = s[i]
#             for j in range(i + 1, N):
#                 char = s[j]
#                 if char in buff_str:
#                     max_len = max(max_len, j - i)
#                     break
#                 else:
#                     buff_str += char
#             else:
#                 max_len = max(max_len, N - i)

#         return max_len

# Solution using dicts instead of strings
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         N: int = len(s)
#         if N <= 1:
#             return N
#         max_len: int = 0
#         buff_dict: dict
#         for i in range(N - 1):
#             buff_dict = {}
#             buff_dict[s[i]] = None
#             for j in range(i + 1, N):
#                 char = s[j]
#                 if char in buff_dict:
#                     max_len = max(max_len, j - i)
#                     break
#                 else:
#                     buff_dict[char] = None
#             else:
#                 max_len = max(max_len, N - i)

#         return max_len


# Solution using a sliding window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)
        max_len = 0
        idxs = [-1 for _ in range(128)]
        i = 0
        for j in range(N):
            if idxs[ord(s[j])] >= i:
                i = idxs[ord(s[j])] + 1
            idxs[ord(s[j])] = j
            max_len = max(max_len, j - i + 1)
        return max_len
