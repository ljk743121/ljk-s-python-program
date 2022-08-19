#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        roma_num = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        roma = ('I','V','X','L','C','D','M')
        ans = 0
        s = [x for x in s]
        while len(s):
            left = s[0]
            try:
                right = s[1]
                if roma.index(left) >= roma.index(right):
                    ans += roma_num[left]
                    s.pop(0)
                else:
                    ans += roma_num[right] - roma_num[left]
                    s.pop(0)
                    s.pop(0)
            except IndexError:
                ans += roma_num[left]
                s.pop(0)
        return ans
# @lc code=end