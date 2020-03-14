#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#
# https://leetcode-cn.com/problems/edit-distance/description/
#
# algorithms
# Hard (56.42%)
# Likes:    562
# Dislikes: 0
# Total Accepted:    31.9K
# Total Submissions: 56.5K
# Testcase Example:  '"horse"\n"ros"'
#
# 给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。
# 
# 你可以对一个单词进行如下三种操作：
# 
# 
# 插入一个字符
# 删除一个字符
# 替换一个字符
# 
# 
# 示例 1:
# 
# 输入: word1 = "horse", word2 = "ros"
# 输出: 3
# 解释: 
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
# 
# 
# 示例 2:
# 
# 输入: word1 = "intention", word2 = "execution"
# 输出: 5
# 解释: 
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')
# 
# 
#

# DP[i][j] word1前i个匹配到word2前j个最少次数
# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1: return len(word2)
        if not word2: return len(word1)

        minStep = [[9999 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        # minStep[0][0] = 0
        # minStep[1][0] = 1
        # minStep[0][1] = 1
        for i in range(len(word1) + 1): minStep[i][0] = i
        for j in range(len(word2) + 1): minStep[0][j] = j

        for m in range(1, len(word1) + 1):
            for n in range(1, len(word2) + 1):
                if word1[m-1] == word2[n-1]:
                    minStep[m][n] = minStep[m-1][n-1]
                else:
                    # 分别插入，删除，替换操作
                    minStep[m][n] = 1 + min(minStep[m-1][n], minStep[m][n-1], minStep[m-1][n-1])
        
        return minStep[len(word1)][len(word2)]


# @lc code=end

