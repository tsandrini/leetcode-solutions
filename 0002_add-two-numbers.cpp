#include <memory>

// // struct ListNode {
// //   int val;
// //   ListNode *next;
// //   ListNode() : val(0), next(nullptr) {}
// //   ListNode(int x) : val(x), next(nullptr) {}
// //   ListNode(int x, ListNode *next) : val(x), next(next) {}
// };
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
  ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
    auto head = std::make_unique<ListNode>(0);
    ListNode *curr = head.get();
    ListNode *prev = curr;

    int carry = 0;
    while (l1 != nullptr || l2 != nullptr || carry != 0) {
      const int sum = carry + (l1 ? l1->val : 0) + (l2 ? l2->val : 0);
      carry = sum / 10;

      curr->next = new ListNode(sum % 10);
      curr = curr->next;

      if (l1 != nullptr) {
        l1 = l1->next;
      }
      if (l2 != nullptr) {
        l2 = l2->next;
      }
    }

    return head->next;
  }
};
