#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0;right = len(nums)-1
        while left <= right:
            mid = (left+right)//2
            guess = nums[mid]
            if target == guess:
                return mid
            elif target < guess:
                right = mid -1
            else:
                left = mid +1
        return left
# @lc code=end

