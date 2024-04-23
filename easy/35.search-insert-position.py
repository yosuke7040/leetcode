#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
import bisect

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # ライブラリ
        # ソートされた配列が前提
        # return bisect.bisect_left(nums, target)

        left = 0
        right = len(nums)

        while left < right:
            middle = ((left + right) // 2)

            # print(left, middle, right)
            if nums[middle] == target:
                return middle

            if nums[middle] > target:
                right = middle
            else:
                left = middle + 1

        return left:

# @lc code=end
