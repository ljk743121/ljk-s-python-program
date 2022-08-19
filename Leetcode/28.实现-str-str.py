#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=='' : return 0
        n = len(needle)
        h = len(haystack)
        for i in range(h):
            if i+n > h:
                return -1
            if haystack[i:i+n] == needle:
                return i
        return -1


# @lc code=end

