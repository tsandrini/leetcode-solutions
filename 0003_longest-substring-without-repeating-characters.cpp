// -------------------------------------------------- //
//  Trivial not really optimal solution using str buffering
// --------------------------------------------------//
// include <algorithm>
// #include <iostream>
// #include <string>
// using namespace std;

// class Solution {
// public:
//   int lengthOfLongestSubstring(string s) {
//     const auto N = s.length();
//     if (N <= 1)
//       return N;
//     int max_len = 0;
//     for (int i = 0; i < N; i++) {
//       string buff = s.substr(i, 1);
//       int j = i + 1;
//       for (; j < N; j++) {
//         const auto c = s[j];
//         if (buff.find(c) != string::npos) {
//           max_len = max(max_len, j - i);
//           // cout << "break: " << max_len << endl;
//           break;
//         } else {
//           buff += s[j];
//           // cout << "non-break: " << buff << endl;
//         }
//       }
//       if (j == N) {
//         max_len = max(max_len, static_cast<int>(N - i));
//         // cout << "outer: " << max_len << endl;
//       }
//     }
//     return max_len;
//   }
// };

// -------------------------------------------------- //
//  Instead of a str buffer use an unordered_set
// --------------------------------------------------//
// #include <algorithm>
// #include <string>
// #include <unordered_set>
// using namespace std;

// class Solution {
// public:
//   int lengthOfLongestSubstring(string s) {
//     const auto N = s.length();
//     int maxLen = 0;
//     unordered_set<char> charTable;
//     int i = 0;
//     for (int j = 0; j < N; j++) {
//       if (charTable.count(s[j]) == 0) {
//         charTable.insert(s[j]);
//         maxLen = max(maxLen, j - i + 1);
//       } else {
//         while (charTable.count(s[j])) {
//           charTable.erase(s[i]);
//           i++;
//         }
//         charTable.insert(s[j]);
//       }
//     }

//     return maxLen;
//   }
// };

// -------------------------------------------------- //
//  Instead of traversing O(n log n) we create a sliding
//  window which is automatically shrinked on duplicates
//  => this results in linear complexity O(n)
// --------------------------------------------------//
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
  int lengthOfLongestSubstring(string s) {
    const auto N = s.length();
    vector<int> idxs(128, -1);
    int maxLen = 0;
    int i = 0;
    for (int j = 0; j < N; j++) {
      if (idxs[s[j]] >= i) {
        i = idxs[s[j]] + 1;
      }
      idxs[s[j]] = j;
      maxLen = max(maxLen, j - i + 1);
    }

    return maxLen;
  }
};
