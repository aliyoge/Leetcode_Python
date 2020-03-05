#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层次遍历
#
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (60.95%)
# Likes:    396
# Dislikes: 0
# Total Accepted:    85K
# Total Submissions: 139.3K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。
# 
# 例如:
# 给定二叉树: [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 返回其层次遍历结果：
# 
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
# 
# 
#

# **BFS,DFS**
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# import collections
# # BFS
# class Solution:
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         if not root: 
#             return []
#         result = []
#         queue = collections.deque()
#         queue.append(root)

#         # visited = set()

#         while queue:
#             levelSize = len(queue)
#             levelList = []

#             for _ in range(levelSize):
#                 node = queue.popleft()
#                 levelList.append(node.val)
#                 if node.left: queue.append(node.left)
#                 if node.right: queue.append(node.right)
            
#             result.append(levelList)

#         return result

# DFS
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        self.result = []
        self._dfs(root, 0)
        return self.result

    def _dfs(self, node: TreeNode, level):
        if not node: 
            return
        
        # 随着深度的增加，不断扩大result的纬度
        if len(self.result) <= level:
            self.result.append([])
        
        self.result[level].append(node.val)

        self._dfs(node.left, level + 1)
        self._dfs(node.right, level + 1)


# @lc code=end

