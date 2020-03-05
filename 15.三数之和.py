#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# https://leetcode-cn.com/problems/3sum/description/
#
# algorithms
# Medium (25.66%)
# Likes:    1852
# Dislikes: 0
# Total Accepted:    164K
# Total Submissions: 638.3K
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0
# ？找出所有满足条件且不重复的三元组。
# 
# 注意：答案中不可以包含重复的三元组。
# 
# 
# 
# 示例：
# 
# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 
# 满足要求的三元组集合为：
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
# 
#
from typing import List

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        # 用于判重
        nums.sort()
        res = set() # 用于判重
        for i, x in enumerate(nums[:-2]):
            # 重要！如果跟前一个数字一样，直接跳过
            if i >=1 and x == nums[i-1]:
                continue
            d = {}
            for m, y in enumerate(nums[i+1:]):
                if y not in d:
                    # 将结果存到字典，在后面的元素里找是否有结果
                    d[-(x+y)] = 1
                else:
                    res.add((x, -(x+y), y))

        # set 转换成list
        return list(map(list, res))

# obj = Solution()
# print(obj.threeSum([-1,0,1,2,-1,-4]))
# @lc code=end

