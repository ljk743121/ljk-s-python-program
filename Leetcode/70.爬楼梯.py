#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
import math

class Solution:
    def climbStairs(self, n: int) -> int:
        s5 = math.sqrt(5)
        return int((1/s5)*(((1+s5)/2)**(n+1)-((1-s5)/2)**(n+1)))
# @lc code=end

