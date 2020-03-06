#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#
# https://leetcode-cn.com/problems/counting-bits/description/
#
# algorithms
# Medium (74.63%)
# Likes:    248
# Dislikes: 0
# Total Accepted:    28.9K
# Total Submissions: 38.7K
# Testcase Example:  '2'
#
# 给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。
# 
# 示例 1:
# 
# 输入: 2
# 输出: [0,1,1]
# 
# 示例 2:
# 
# 输入: 5
# 输出: [0,1,1,2,1,2]
# 
# 进阶:
# 
# 
# 给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？
# 要求算法的空间复杂度为O(n)。
# 你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的 __builtin_popcount）来执行此操作。
# 
# 
#

# @lc code=start
class Solution:
    def countBits(self, num: int) -> List[int]:
        # 包含0，所以要初始化num + 1个位的数组
        result = [0 for _ in range(num + 1)]
        # 从1开始迭代
        for i in range(num + 1)[1:]:
            # 实际上result中的第几位就是存的数字几的1位数
            # 这里i & (i - 1)的1的位数始终比i小一个
            result[i] = result[i & (i - 1)] + 1
        return result

        
# @lc code=end

