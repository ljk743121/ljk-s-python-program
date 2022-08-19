#
# @lc app=leetcode.cn id=640 lang=python3
#
# [640] 求解方程
#

# @lc code=start
class Solution:
    def solveEquation(self, equation: str) -> str:
        equation = equation.replace("-","+-")+"+"
        if equation[0]!="+":
            equation = '+'+equation
        sign,i,num,xnum,memory = 1,0,0,0,''
        while i<len(equation):
            if equation[i] == '=':
                sign = -1
                equation = equation.replace('=','+')
                continue
            if equation[i]=="+":
                i += 1
                if i>=len(equation): break
                while equation[i]!="+":
                    if equation[i]=='=':
                        num += int(memory)*sign
                        break
                    if equation[i]=="x":
                        if memory=='':
                            xnum += 1*sign
                        elif memory=='-':
                            xnum += -1*sign
                        else:
                            xnum += int(memory)*sign
                        i += 1
                        break
                    else:
                        memory = memory+equation[i]
                    i += 1
                else:
                    if memory!='': num += int(memory)*sign
                memory = ''
        if xnum==0:
            if num==0:
                return 'Infinite solutions'
            else:
                return 'No solution'
        else:
            return 'x='+str(-num//xnum)
# @lc code=end

