from typing import List

# ----------------------------------
# Two pointer method
# ----------------------------------
# Status: Accepted (2094/2094)
# Runtime: 82 ms, faster than 90.40% of Python3 submissions.
# Memory Usage: 16.7 MB, less than 16.68% of Python3 submissions.
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         N: int = len(nums1)
#         M: int = len(nums2)
#         result_len: int = len(nums1) + len(nums2)
#         is_odd: bool = result_len % 2 == 1
#         upper_bound: int = result_len // 2 if is_odd else (result_len // 2)
#         i: int = 0
#         j: int = 0
#         k: int = 0
#         out: List[int] = []
#         while (i < N or j < M) and (k < (upper_bound + 1)):
#             k += 1
#             if i == N:
#                 out.append(nums2[j])
#                 j += 1
#             elif j == M:
#                 out.append(nums1[i])
#                 i += 1
#             elif nums1[i] < nums2[j]:
#                 out.append(nums1[i])
#                 i += 1
#             else:
#                 out.append(nums2[j])
#                 j += 1
#         return out[-1] if is_odd else ((out[-1] + out[-2]) / 2)


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        if len1 > len2:
            return self.findMedianSortedArrays(nums2, nums1)

        left = 0
        right = len1
        out_median_idx = (len1 + len2 + 1) // 2
        # Basically binary search using two windows
        while left <= right:
            m = (left + right) // 2

            m1 = m
            m2 = out_median_idx - m1

            left_partition1 = nums1[m1 - 1] if m1 > 0 else float("-inf")
            left_partition2 = nums2[m2 - 1] if m2 > 0 else float("-inf")

            right_partition1 = nums1[m1] if m1 < len1 else float("inf")
            right_partition2 = nums2[m2] if m2 < len2 else float("inf")

            if (
                left_partition1 <= right_partition2
                and left_partition2 <= right_partition1
            ):
                if (len1 + len2) % 2 == 0:
                    return (
                        max(left_partition1, left_partition2)
                        + min(right_partition1, right_partition2)
                    ) / 2.0
                else:
                    return max(left_partition1, left_partition2)
            elif left_partition1 > right_partition2:
                right = m - 1
            else:
                left = m + 1

        return 0.0
