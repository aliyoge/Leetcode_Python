#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
# https://leetcode-cn.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (73.45%)
# Likes:    779
# Dislikes: 0
# Total Accepted:    80.6K
# Total Submissions: 109.6K
# Testcase Example:  '3'
#
# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
# 
# 例如，给出 n = 3，生成结果为：
# 
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
# 
# 
#

# **DFS&BFS&剪枝**
from typing import List
# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.result = []
        self._gen(0, 0, n, "")
        return self.result

    def _gen(self, left, right, n, words):
            if left == n and right == n:
                self.result.append(words)
                return

            if left < n:
                self._gen(left + 1, right, n, words + "(")
            if right < n and left > right:
                self._gen(left, right + 1, n, words + ")")
        
test = Solution()
test.generateParenthesis(3)


# @lc code=end

