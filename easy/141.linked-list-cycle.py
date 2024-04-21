#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from typing import Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = {}
        while head != None:
            if head in seen:
                return True
            seen[head] = True
            head = head.next
        return False


# @lc code=end

if __name__ == "__main__":
    # デバッグ用の入力を作成
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = head  # サイクルを作成

    solution = Solution()
    result = solution.hasCycle(head)
    print(result)
