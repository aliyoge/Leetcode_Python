#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#
# https://leetcode-cn.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (56.33%)
# Likes:    386
# Dislikes: 0
# Total Accepted:    39.2K
# Total Submissions: 69.5K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
# 
# k 是一个正整数，它的值小于或等于链表的长度。
# 
# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
# 
# 示例 :
# 
# 给定这个链表：1->2->3->4->5
# 
# 当 k = 2 时，应当返回: 2->1->4->3->5
# 
# 当 k = 3 时，应当返回: 3->2->1->4->5
# 
# 说明 :
# 
# 
# 你的算法只能使用常数的额外空间。
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
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
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        

# 后插法
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummp = ListNode(-1)
        dummp.next = head
        pre = dummp
        tail = dummp

        while True:
            count = k # 调整完一个子序列后重置count
            while count and tail: # 将tail移动到子序列最后
                count -= 1
                tail = tail.next
            
            if not tail: # 如果子序列不够k长
                break

            head = pre.next # 保存移动前子序列第一个node，因为它移动后会变成最后一个，也是下一个子序列的前一个
            while pre.next != tail: # 将tail移动到子序列最前面后停止
                cur = pre.next
                pre.next = cur.next
                cur.next = tail.next
                tail.next = cur
            pre = head
            tail = head
            
        return dummp.next
        

# @lc code=end

