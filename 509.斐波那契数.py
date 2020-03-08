#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#
# https://leetcode-cn.com/problems/fibonacci-number/description/
#
# algorithms
# Easy (66.20%)
# Likes:    97
# Dislikes: 0
# Total Accepted:    40.4K
# Total Submissions: 60.9K
# Testcase Example:  '2'
#
# 斐波那契数，通常用 F(n) 表示，形成的序列称为斐波那契数列。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：
# 
# F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
# 
# 
# 给定 N，计算 F(N)。
# 
# 
# 
# 示例 1：
# 
# 输入：2
# 输出：1
# 解释：F(2) = F(1) + F(0) = 1 + 0 = 1.
# 
# 
# 示例 2：
# 
# 输入：3
# 输出：2
# 解释：F(3) = F(2) + F(1) = 1 + 1 = 2.
# 
# 
# 示例 3：
# 
# 输入：4
# 输出：3
# 解释：F(4) = F(3) + F(2) = 2 + 1 = 3.
# 
# 
# 
# 
# 提示：
# 
# 
# 0 ≤ N ≤ 30
# 
# 
#

# @lc code=start
# 递推
class Solution:
    def fib(self, N: int) -> int:
        if N <= 1: return N

        F = {}
        F[0] = 0
        F[1] = 1

        for i in range(N+1)[2:]:
            F[i] = F[i - 1] + F[i - 2]

        return F[N]

# 递归记忆化优化
# class Solution:
#     def fib(self, N: int) -> int:
#         mem = {} 
#         return self._fib(N, mem)
#     # 记忆化，避免重复计算
#     def _fib(self, N, mem):
#         if N <= 1:
#             return N
#         if N not in mem:
#             mem[N] = self._fib(N - 1, mem) + self._fib(N - 2, mem)
#         return mem[N]

# @lc code=end

