#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/description/
#
# algorithms
# Hard (29.17%)
# Likes:    169
# Dislikes: 0
# Total Accepted:    12.8K
# Total Submissions: 43.8K
# Testcase Example:  '2\n[2,4,1]'
#
# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
# 
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
# 
# 注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 
# 示例 1:
# 
# 输入: [2,4,1], k = 2
# 输出: 2
# 解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
# 
# 
# 示例 2:
# 
# 输入: [3,2,6,5,0,3], k = 2
# 输出: 7
# 解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4
# 。
# 随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
# 
# 
#

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or k == 0 or len(prices) < 2: return 0

        maxProfit = 0
        l = len(prices)
        # 这里k+1，因为有0~k，k+1种情况
        # 注意，这里考虑边界问题，即k <= len(prices)
        # 这样在k = 1000000000 的测试样例会爆内存
        # k = min(k, l) # 这样还是不行

        # 当k > len(prices)时可以使用贪心算法
        if k > l:
            for i in range(1, l):
                diff = prices[i] - prices[i - 1]
                maxProfit += (diff if diff > 0 else 0) 
            return maxProfit

        profits = [[[0 for _ in range(2)] for _ in range(k+1)] for _ in range(l)]
        profits[0][0][0], profits[0][0][1] = 0, -prices[0]
        # 这里k+1，因为有0~k，k+1种情况
        for m in range(1, k+1):
            for n in range(2):
                profits[0][m][n] = -99999
        
        
        # 第i天，卖了m次的情况
        for i in range(1, l):
            # 这里k+1，因为有0~k，k+1种情况
            for m in range(k+1):
                if m == 0:
                    profits[i][0][0] = profits[i-1][0][0]
                    profits[i][0][1] = max(profits[i-1][0][1], -prices[i]) 
                else:
                    profits[i][m][0] = max(profits[i-1][m][0], profits[i-1][m-1][1] + prices[i])
                    profits[i][m][1] = max(profits[i-1][m][1], profits[i-1][m][0] - prices[i])
                
                maxProfit = max(maxProfit, profits[i][m][0])

        return maxProfit
# @lc code=end

