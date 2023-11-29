#include <string>
using namespace std;

// Status: Accepted (142/142)
// Runtime: 7 ms, faster than 93.36% of C++ submissions.
// Memory Usage: 15.8 MB, less than 49.10% of C++ submissions.
//
// So this is a refined version of my first naive implementation with a
// bunch of optimizations. ChatGPT is telling me that I've basically created a
// modified version of the Manacher's algorithm???? ig okay
class Solution {
public:
  string longestPalindrome(string s) {
    if (s.length() < 2)
      return s;

    // Instead of regeinx
    string processedStr = "#";
    processedStr.reserve(2 * s.length() + 1);
    for (char c : s) {
      processedStr += c;
      processedStr += '#';
    }
    s = processedStr;

    const int N = s.length();
    int longestLen = 1;
    string longestStr = s.substr(1, 2);

    for (int i = 1; i < N - 1; i++) {
      int j = 1;

      while ((i - j >= 0) && (i + j < N) && (s[i - j] == s[i + j])) {
        j++;
      }

      if (j - 1 > longestLen) {
        longestLen = j - 1;
        longestStr = s.substr(i - longestLen, 2 * longestLen + 1);
      }

      if (longestLen >= N - i - 1)
        break;
    }

    longestStr.erase(remove(longestStr.begin(), longestStr.end(), '#'),
                     longestStr.end());

    return longestStr;
  }
};
