#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]
        ans = []
        try:
            for i in range(len(first)):
                for j in range(1,len(strs)):
                    if first[i]==strs[j][i]:
                        pass
                    else:
                        return ''.join(ans)
                ans.append(first[i])
        except Exception:
            pass
        finally:
            return ''.join(ans)
# @lc code=end

