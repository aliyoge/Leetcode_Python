#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#
# https://leetcode-cn.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (64.48%)
# Likes:    423
# Dislikes: 0
# Total Accepted:    74.2K
# Total Submissions: 115.1K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
# 
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
# 
# 
# 
# 示例:
# 
# 给定 1->2->3->4, 你应该返回 2->1->4->3.
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 递归
# class Solution:
#     def swapPairs(self, head: ListNode) -> ListNode:
#         if head == None or head.next == None:
#             return head

#         first = head
#         second = head.next

#         first.next = self.swapPairs(second.next)
#         second.next = first

#         return second

# 迭代
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 创建虚拟节点，当做head的前面一个节点
        dummpNode = ListNode(-1)
        dummpNode.next = head

        preNode = dummpNode

        # 保证要交换位置的两个node都存在
        while head and head.next:
            # 取出要交换的两个node
            firstNode = head
            secondNode = head.next

            # 进行交换
            preNode.next = secondNode
            firstNode.next = secondNode.next
            secondNode.next = firstNode

            # 继续交换接下来两个，并且保存前一个node
            head = firstNode.next
            preNode = firstNode
        
        return dummpNode.next

# @lc code=end

