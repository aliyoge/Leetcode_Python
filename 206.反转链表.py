#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 迭代
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         cur = head
#         pre = None # 注意头结点反转后指向None
#         while cur: 
#             tmp = cur.next # 每次改变cur.next节点，所以要保存
#             cur.next = pre
#             pre= cur
#             cur = tmp
#         return pre

# 递归
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 定义递归方法
        def helper(headNode):
            if headNode == None or headNode.next == None:
                return headNode, headNode

            # 返回当前head的前一个元素，整个原始列表最后一个元素
            pre, last= helper(headNode.next)

            pre.next = headNode
            headNode.next = None
            return headNode, last

        _, last = helper(head)     
        return last

# @lc code=end

