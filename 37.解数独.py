#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#
# https://leetcode-cn.com/problems/sudoku-solver/description/
#
# algorithms
# Hard (59.80%)
# Likes:    333
# Dislikes: 0
# Total Accepted:    20.4K
# Total Submissions: 34K
# Testcase Example:  '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
#
# 编写一个程序，通过已填充的空格来解决数独问题。
# 
# 一个数独的解法需遵循如下规则：
# 
# 
# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
# 
# 
# 空白格用 '.' 表示。
# 
# 
# 
# 一个数独。
# 
# 
# 
# 答案被标成红色。
# 
# Note:
# 
# 
# 给定的数独序列只包含数字 1-9 和字符 '.' 。
# 你可以假设给定的数独只有唯一解。
# 给定数独永远是 9x9 形式的。
# 
# 
#
from typing import List

# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or len(board) == 0: return
        self.initNums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.solve(board)
    
    def solve(self, board):
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == '.':
                    for num in self.initNums:
                        # 判断数字有效则填入
                        if self.isValid(board, row, col, num):
                            board[row][col] = num
                            if self.solve(board):
                                return True
                            else:
                                # 回溯的步骤，还原刚才填的
                                board[row][col] = '.'
                    # 如果循完都没有找到isValid那么，solve返回False，到上一步进行回溯
                    return False
        # 最后循环完要返回True
        return True


    def isValid(self, board, row, col, num):
        for i in range(9):
            # 先判断这一行有没有
            if board[row][i] != '.' and board[row][i] == num: 
                return False 
            # 再判断这一列有没有
            if board[i][col] != '.' and board[i][col] == num: 
                return False
            # 再判断小9宫格有没有
            # 1, 9宫格中的row
            subRow = row // 3 * 3 + i // 3
            subCol = col // 3 * 3 + i % 3
            if board[subRow][subCol] != '.' and board[subRow][subCol] == num: 
                return False
        return True

# test = Solution()
# sudoku = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# test.solveSudoku(sudoku)
# print(sudoku)


# @lc code=end

