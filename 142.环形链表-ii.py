#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#
# https://leetcode-cn.com/problems/linked-list-cycle-ii/description/
#
# algorithms
# Medium (48.65%)
# Likes:    369
# Dislikes: 0
# Total Accepted:    53.1K
# Total Submissions: 109.1K
# Testcase Example:  '[3,2,0,-4]\n1'
#
# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
# 
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
# 
# 说明：不允许修改给定的链表。
# 
# 
# 
# 示例 1：
# 
# 输入：head = [3,2,0,-4], pos = 1
# 输出：tail connects to node index 1
# 解释：链表中有一个环，其尾部连接到第二个节点。
# 
# 
# 
# 
# 示例 2：
# 
# 输入：head = [1,2], pos = 0
# 输出：tail connects to node index 0
# 解释：链表中有一个环，其尾部连接到第一个节点。
# 
# 
# 
# 
# 示例 3：
# 
# 输入：head = [1], pos = -1
# 输出：no cycle
# 解释：链表中没有环。
# 
# 
# 
# 
# 
# 
# 进阶：
# 你是否可以不用额外空间解决此题？
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 哈希方法
# class Solution:
#     def detectCycle(self, head: ListNode) -> ListNode:
#         visited = set() 
#         node = head
#         while node:
#             if node in visited:
#                 return node
#             visited.add(node)
#             node = node.next
#         return None
            
# 快慢指针
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast, slow = head, head

        while True:
            if fast == None or fast.next == None:
                return
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                break

        # 错误，此处不能用while判断相等
        # while fast != slow:
        #     if fast == None or fast.next == None:
        #         return
        #     fast = fast.next.next
        #     slow = slow.next

        fast = head

        while fast != slow:
            fast, slow = fast.next, slow.next

        return fast

# @lc code=end

