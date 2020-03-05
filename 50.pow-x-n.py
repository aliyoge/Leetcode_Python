#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#
# https://leetcode-cn.com/problems/powx-n/description/
#
# algorithms
# Medium (33.96%)
# Likes:    271
# Dislikes: 0
# Total Accepted:    55.3K
# Total Submissions: 162.5K
# Testcase Example:  '2.00000\n10'
#
# 实现 pow(x, n) ，即计算 x 的 n 次幂函数。
# 
# 示例 1:
# 
# 输入: 2.00000, 10
# 输出: 1024.00000
# 
# 
# 示例 2:
# 
# 输入: 2.10000, 3
# 输出: 9.26100
# 
# 
# 示例 3:
# 
# 输入: 2.00000, -2
# 输出: 0.25000
# 解释: 2^-2 = 1/2^2 = 1/4 = 0.25
# 
# 说明:
# 
# 
# -100.0 < x < 100.0
# n 是 32 位有符号整数，其数值范围是 [−2^31, 2^31 − 1] 。
# 
# 
#

# @lc code=start
# ** 递归&分治 **
# 迭代
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # n<0的情况，将n转换成大于0的情况
        if n < 0:
            x = 1 / x
            n = -n 
        pow = 1
        # 实际上是减少了相乘的次数
        # 中间跨级平方
        while n:
            # 如果是奇数就会跳过这一步，那么下面的
            # 第一次x *= x就是处理奇数多出来的那个x
            if n & 1:
                pow *= x
            x *= x
            # 右移一位，等于除以2
            n >>= 1 
        return pow


# 递归
# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         if not n:
#             return 1;
#         # 如果n小于0，那么要求倒数
#         if n < 0:
#             return 1 / self.myPow(x, -n)
#         if n % 2:
#             return x * self.myPow(x, n - 1)
#         return self.myPow(x*x, n/2)

# @lc code=end

