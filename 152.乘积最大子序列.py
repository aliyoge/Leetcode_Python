#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子序列
#
# https://leetcode-cn.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (37.31%)
# Likes:    411
# Dislikes: 0
# Total Accepted:    38.1K
# Total Submissions: 101.8K
# Testcase Example:  '[2,3,-2,4]'
#
# 给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。
# 
# 示例 1:
# 
# 输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
# 
# 
# 示例 2:
# 
# 输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
# 
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        maxValue = 0
        # 二维0存放正的最大值，1存放负的最大值
        eleValues = [[0 for _ in range(2)] for _ in range(len(nums))]

        for i in range(len(nums)):
            # 前一个最大正数
            preMax = 0 if i < 1 else eleValues[i - 1][0]
            # 前一个最大负数
            preMin = 0 if i < 1 else eleValues[i - 1][1]

            # 如果当前值大于0
            if nums[i] >= 0:
                eleValues[i][0] = nums[i] * (1 if preMax == 0 else preMax)
                eleValues[i][1] = nums[i] * preMin
            # 如果当前值小于0
            else:
                eleValues[i][0] = nums[i] * preMin
                eleValues[i][1] = nums[i] * (1 if preMax == 0 else preMax)

            # 更新最大值
            if eleValues[i][0] > maxValue:
                maxValue = eleValues[i][0]

        return maxValue


# @lc code=end

