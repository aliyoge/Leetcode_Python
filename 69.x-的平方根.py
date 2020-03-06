#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#
# https://leetcode-cn.com/problems/sqrtx/description/
#
# algorithms
# Easy (37.56%)
# Likes:    317
# Dislikes: 0
# Total Accepted:    100.4K
# Total Submissions: 267K
# Testcase Example:  '4'
#
# 实现 int sqrt(int x) 函数。
# 
# 计算并返回 x 的平方根，其中 x 是非负整数。
# 
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
# 
# 示例 1:
# 
# 输入: 4
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842..., 
# 由于返回类型是整数，小数部分将被舍去。
# 
# 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        # 一个数的平方根最多不会超过它的一半
        l, r, res = 1, x // 2, 0
        while l <= r:
            mid = (l + r) // 2
            if mid == x // mid:
                return mid
            if mid > x // mid:
                r = mid - 1
            if mid < x // mid:
                l = mid + 1
                # 注意，这里要选小的那个中位数，因为题目要求返回的是整数部分
                res = mid
        return res

# @lc code=end

