#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in range(len(digits)):
            num = num*10+digits[i]
        num += 1
        return list(map(int,[i for i in str(num)]))
# @lc code=end

