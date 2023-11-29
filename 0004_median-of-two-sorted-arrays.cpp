#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
  double findMedianSortedArrays(vector<int> &nums1, vector<int> &nums2) {
    if (nums1.size() > nums2.size())
      swap(nums2, nums1);

    const int len1 = nums1.size();
    const int len2 = nums2.size();

    int left = 0;
    int right = len1;
    const int out_median_idx = (len1 + len2 + 1) / 2;
    while (left <= right) {
      const int m = (left + right) / 2;

      int m1 = m;
      int m2 = out_median_idx - m1;

      int left_partition1 = m1 > 0 ? nums1[m1 - 1] : INT_MIN;
      int left_partition2 = m2 > 0 ? nums2[m2 - 1] : INT_MIN;

      int right_partition1 = m1 < len1 ? nums1[m1] : INT_MAX;
      int right_partition2 = m2 < len2 ? nums2[m2] : INT_MAX;

      if (left_partition1 <= right_partition2 &&
          left_partition2 <= right_partition1) {
        if ((len1 + len2) % 2 == 0) {
          return (max(left_partition1, left_partition2) +
                  min(right_partition1, right_partition2)) /
                 2.0;
        } else {
          return max(left_partition1, left_partition2);
        }
      } else if (left_partition1 > right_partition2) {
        right = m - 1;
      } else {
        left = m + 1;
      }
    }

    return 0.0;
  }
};
