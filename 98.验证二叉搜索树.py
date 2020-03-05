#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#
# https://leetcode-cn.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (29.05%)
# Likes:    427
# Dislikes: 0
# Total Accepted:    71.9K
# Total Submissions: 247.2K
# Testcase Example:  '[2,1,3]'
#
# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
# 
# 假设一个二叉搜索树具有如下特征：
# 
# 
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
# 
# 
# 示例 1:
# 
# 输入:
# ⁠   2
# ⁠  / \
# ⁠ 1   3
# 输出: true
# 
# 
# 示例 2:
# 
# 输入:
# ⁠   5
# ⁠  / \
# ⁠ 1   4
# / \
# 3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
# 根节点的值为 5 ，但是其右子节点值为 4 。
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 中序遍历
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def inorder(head):
            if head == None:
                return []
            return inorder(head.left) + [head.val] + inorder(head.right)
        
        inorderList = inorder(root)
        return inorderList == list(sorted(set(inorderList)))
    
# 递归
# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#         def helper(head, min, max):
#             if not head:
#                 return True                
#             # 等于也不可以
#             if min != None and head.val <= min:
#                 return False
#             if max != None and head.val >= max:
#                 return False
            
#             return helper(head.left, min, head.val) and helper(head.right, head.val, max)
        
#         return helper(root, None, None)

# @lc code=end

