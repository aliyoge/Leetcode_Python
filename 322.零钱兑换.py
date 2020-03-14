#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#
# https://leetcode-cn.com/problems/coin-change/description/
#
# algorithms
# Medium (37.65%)
# Likes:    484
# Dislikes: 0
# Total Accepted:    62.2K
# Total Submissions: 161.3K
# Testcase Example:  '[1,2,5]\n11'
#
# 给定不同面额的硬币 coins 和一个总金额
# amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
# 
# 示例 1:
# 
# 输入: coins = [1, 2, 5], amount = 11
# 输出: 3 
# 解释: 11 = 5 + 5 + 1
# 
# 示例 2:
# 
# 输入: coins = [2], amount = 3
# 输出: -1
# 
# 说明:
# 你可以认为每种硬币的数量是无限的。
# 
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins: return -1
        if not amount: return 0
        # 状态定义：从0块到amount块，每一步最小count
        # 递推方程：F[i] = min(f[i - coin[0]] + 1 ~ F[i - coins[k]] + 1)
        minCounts = [99999 for _ in range(amount + 1)]
        minCounts[0] = 0
        for i in range(len(coins)):
            if amount >= coins[i]:
                # 只需要一个硬币的情况
                minCounts[coins[i]] = 1
        
        for i in range(1, amount + 1):
            loopMin = minCounts[i]
            for k in range(len(coins)):
                # 要保证 i - coins[k] >= 0
                if i >= coins[k]:
                    curMin = minCounts[i - coins[k]] + 1
                    if curMin < loopMin:
                        loopMin = curMin
            minCounts[i] = loopMin

        return -1 if minCounts[amount] == 99999 else minCounts[amount]
        
# @lc code=end

