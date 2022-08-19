#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        r = []
        for i in s:
            asc = ord(i)
            if 48<=asc<=57 or 97<=asc<=122 :
                r.append(i)
        if r == r[::-1]:
            return True
        else:
            return False
# @lc code=end

