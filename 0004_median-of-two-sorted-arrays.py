from typing import List


# Status: Accepted (2094/2094)
# Runtime: 82 ms, faster than 90.40% of Python3 submissions.
# Memory Usage: 16.7 MB, less than 16.68% of Python3 submissions.
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        N: int = len(nums1)
        M: int = len(nums2)
        result_len: int = len(nums1) + len(nums2)
        is_odd: bool = result_len % 2 == 1
        upper_bound: int = result_len // 2 if is_odd else (result_len // 2)
        i: int = 0
        j: int = 0
        k: int = 0
        out: List[int] = []
        while (i < N or j < M) and (k < (upper_bound + 1)):
            k += 1
            if i == N:
                out.append(nums2[j])
                j += 1
            elif j == M:
                out.append(nums1[i])
                i += 1
            elif nums1[i] < nums2[j]:
                out.append(nums1[i])
                i += 1
            else:
                out.append(nums2[j])
                j += 1
        return out[-1] if is_odd else ((out[-1] + out[-2]) / 2)
