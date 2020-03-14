#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长上升子序列
#
# https://leetcode-cn.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (44.10%)
# Likes:    446
# Dislikes: 0
# Total Accepted:    54.2K
# Total Submissions: 122.6K
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# 给定一个无序的整数数组，找到其中最长上升子序列的长度。
# 
# 示例:
# 
# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4 
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
# 
# 说明:
# 
# 
# 可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
# 你算法的时间复杂度应该为 O(n^2) 。
# 
# 
# 进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
# 
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        

# 维护上升序列-迭代
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         if not nums or len(nums) < 1: return 0
#         risingList = []
#         for i in range(len(nums)):
#             if i == 0: 
#                 risingList.append(nums[i]) 
#                 continue
#             # 如果大于于上升序列最后一个,直接加在最后
#             if nums[i] > risingList[-1]:
#                 risingList.append(nums[i])
#             else: # 否则替换上升队列里面的数
#                 for m in range(len(risingList)):
#                     if nums[i] <= risingList[m]:
#                         risingList.pop(m)
#                         risingList.insert(m, nums[i])
#                         break

#         return len(risingList)
        
# @lc code=end

