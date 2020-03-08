#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#
# https://leetcode-cn.com/problems/triangle/description/
#
# algorithms
# Medium (63.70%)
# Likes:    325
# Dislikes: 0
# Total Accepted:    43K
# Total Submissions: 67.4K
# Testcase Example:  '[[2],[3,4],[6,5,7],[4,1,8,3]]'
#
# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
# 
# 例如，给定三角形：
# 
# [
# ⁠    [2],
# ⁠   [3,4],
# ⁠  [6,5,7],
# ⁠ [4,1,8,3]
# ]
# 
# 
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
# 
# 说明：
# 
# 如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
# 
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle or len(triangle) == 0: return 0
        # 记录每一行每个元素，从它下面到这里的最小值
        rowMin = [0 for _ in range(len(triangle))]

        # 从最后一行开始迭代，
        for row in range((len(triangle) - 1), -1, -1):
            for col in range(row + 1):
                if row >= len(triangle) - 1:
                    # 最后一行, 每一个到该元素的最小值是它自己
                    rowMin[col] = triangle[row][col]
                else:
                    # 否则是它下一行那两个能到达它的总步数小的那个+它自己
                    # 这里只用一维数组来保存每一行的最小
                    # 因为从最前面开始，用过了就可以覆盖，后面用不上
                    rowMin[col] = min(rowMin[col], rowMin[col + 1]) + triangle[row][col]

        return rowMin[0]

# @lc code=end

