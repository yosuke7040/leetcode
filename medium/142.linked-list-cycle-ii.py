#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#
# from typing import Optional


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head):
        seen = {}
        idx = 0
        while head != None:
            if head in seen:
                # print(seen)
                # print(f"tail connects to node index {seen[head]}")
                return head
            seen[head] = idx
            head = head.next
            idx += 1

        # print("no cycle")
        return None


# @lc code=end


# if __name__ == "__main__":
#     # デバッグ用の入力を作成
#     head = ListNode(3)
#     head.next = ListNode(2)
#     head.next.next = ListNode(0)
#     head.next.next.next = ListNode(-4)
#     head.next.next.next.next = head.next  # サイクルを作成

#     solution = Solution()
#     result = solution.detectCycle(head)
#     # print(result)
