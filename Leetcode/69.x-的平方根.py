#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        ans = 0
        for i in range(x+1):
            if i*i > x:
                return ans
            else:
                ans = i
        return ans
# @lc code=end

