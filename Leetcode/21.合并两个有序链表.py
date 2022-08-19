#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
        ans = []
        for i in range(max(len(list1),len(list2))):
            try:
                if list1[i] >= list2[i]:
                    ans.append(list2[i]);ans.append(list1[i])
                else:
                    ans.append(list1[i]);ans.append(list2[i])
            except IndexError:
                if i >= len(list1):
                    ans.append(list2[i])
                else:
                    ans.append(list1[i])
        return ans
'''

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next            
            prev = prev.next

        # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
        prev.next = l1 if l1 is not None else l2

        return prehead.next
# @lc code=end

