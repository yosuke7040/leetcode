#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set_num1 = set(nums1)
        set_num2 = set(nums2)

        print(set_num1)
        print(set_num2)
        ans = set_num1 & set_num2

        return ans


# @lc code=end
