#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N皇后
#
# https://leetcode-cn.com/problems/n-queens/description/
#
# algorithms
# Hard (67.94%)
# Likes:    345
# Dislikes: 0
# Total Accepted:    28.4K
# Total Submissions: 41.7K
# Testcase Example:  '4'
#
# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
# 
# 
# 
# 上图为 8 皇后问题的一种解法。
# 
# 给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
# 
# 每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
# 
# 示例:
# 
# 输入: 4
# 输出: [
# ⁠[".Q..",  // 解法 1
# ⁠ "...Q",
# ⁠ "Q...",
# ⁠ "..Q."],
# 
# ⁠["..Q.",  // 解法 2
# ⁠ "Q...",
# ⁠ "...Q",
# ⁠ ".Q.."]
# ]
# 解释: 4 皇后问题存在两个不同的解法。
# 
# 
#

from typing import List

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n < 1: return []
        self.cols, self.xy_sum, self.xy_dif = set(), set(), set()
        self.result = []
        self._dfs(n, [])
        return self._generate_result(n)


    def _dfs(self, n, curState):
        row = len(self.cols)
        if row == n:
            # !! 不能用set来记录顺序，以为set没有顺序
            # self.result.append(list(self.cols))
            self.result.append(curState)
            return
            
        for col in range(n):
            if col in self.cols or col + row in self.xy_sum or row - col in self.xy_dif:
                continue

            self.cols.add(col)
            self.xy_sum.add(col + row)
            self.xy_dif.add(row - col)

            self._dfs(n, curState + [col])

            # 前面递归完成后
            # 1, 如果全部走完没问题
            # 2, 走不下去，有问题
            # 都会重新走前一步
            # 所以要重置之前添加的数据
            self.cols.remove(col)
            self.xy_sum.remove(col + row)
            self.xy_dif.remove(row - col)

    def _generate_result(self, n):
        board = []        
        for res in self.result:
            for col in res:
                board.append("."*col + "Q" + "."*(n-col-1))
        return [board[i: i+n] for i in range(0, len(board), n)]

        
test = Solution()
print(test.solveNQueens(4))       
        


# @lc code=end

