#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # print(root)

        def dfs(root, depth):
            if root is None:
                return depth
            depth += 1

            return max(dfs(root.right, depth), dfs(root.left, depth))

        return dfs(root, 0)


# @lc code=end
