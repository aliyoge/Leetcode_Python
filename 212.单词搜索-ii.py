#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#
# https://leetcode-cn.com/problems/word-search-ii/description/
#
# algorithms
# Hard (39.24%)
# Likes:    112
# Dislikes: 0
# Total Accepted:    10K
# Total Submissions: 25.6K
# Testcase Example:  '[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n' +
#  '["oath","pea","eat","rain"]'
#
# 给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。
# 
# 
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。
# 
# 示例:
# 
# 输入: 
# words = ["oath","pea","eat","rain"] and board =
# [
# ⁠ ['o','a','a','n'],
# ⁠ ['e','t','a','e'],
# ⁠ ['i','h','k','r'],
# ⁠ ['i','f','l','v']
# ]
# 
# 输出: ["eat","oath"]
# 
# 说明:
# 你可以假设所有输入都由小写字母 a-z 组成。
# 
# 提示:
# 
# 
# 你需要优化回溯算法以通过更大数据量的测试。你能否早点停止回溯？
# 如果当前单词不存在于所有单词的前缀中，则可以立即停止回溯。什么样的数据结构可以有效地执行这样的操作？散列表是否可行？为什么？
# 前缀树如何？如果你想学习如何实现一个基本的前缀树，请先查看这个问题： 实现Trie（前缀树）。
# 
# 
#
from typing import List
import collections
# **Trie数**
# @lc code=start
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
      if not board or len(board) == 0: return [] 
      if not words or len(words) == 0: return []

      self.END_OF_WORD = '#'
      self.result = set()
      root = collections.defaultdict()

      # 将单词都存入Trie树
      for word in words:
        node = root
        for letter in word:
          if letter not in node:
            node[letter] = collections.defaultdict()
          node = node[letter]
        node[self.END_OF_WORD] = self.END_OF_WORD
      
      # 对矩阵进行DFS, 判断各种路径是否存在Trie中
      for row in range(len(board)):
        for col in range(len(board[row])):
          if board[row][col] in root:
            self._dfs(board, row, col, "", root)
      
      return list(self.result)

    # 深度查找方法
    def _dfs(self, board, row, col, curChars, curNode):
      curChars += board[row][col]
      curNode = curNode[board[row][col]]

      # 如果找到单词了，则终止
      if self.END_OF_WORD in curNode:
        self.result.add(curChars)
        # !!! 注意，这里不能停止，因为有的单词的前缀也是一个单词，比如move, movement
        # 不能锁扫到move就停止扫了
        # return

      # 继续深度查找，先保存当前格子的值，然后将格子标记一下
      tmp = board[row][col]
      board[row][col] = "@"

      # 查找格子上下左右路径
      # 上方格子
      if row - 1 >= 0 and board[row - 1][col] != "@" and board[row - 1][col] in curNode:
        self._dfs(board, row - 1, col, curChars, curNode)
      # 下方格子
      if row + 1 < len(board) and board[row + 1][col] != "@" and board[row + 1][col] in curNode:
        self._dfs(board, row + 1, col, curChars, curNode)
      # 左边格子
      if col - 1 >= 0 and board[row][col - 1] != "@" and board[row][col - 1] in curNode:
        self._dfs(board, row, col - 1, curChars, curNode)
      # 右边格子
      if col + 1 < len(board[0]) and board[row][col + 1] != "@" and board[row][col + 1] in curNode:
        self._dfs(board, row, col + 1, curChars, curNode)

      # 回溯，还原格子
      board[row][col] = tmp

# test = Solution()
# print(test.findWords([["a","b"]], ["ba"]))
      

# @lc code=end

