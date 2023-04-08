# -*- coding: utf-8 -*- #
# Name        : 1143_longestCommonSubsequence.py
# Author      : haishen yao
# Time        : 2023/4/8 17:38
# Description : 1143. 最长公共子序列

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        动态规划，讲解：https://leetcode.cn/problems/longest-common-subsequence/solution/shi-pin-jiang-jie-shi-yong-dong-tai-gui-hua-qiu-ji/
        :param text1:
        :param text2:
        :return:
        '''
        len_t1 = len(text1)
        len_t2 = len(text2)
        dp = [[0]*(len_t2+1) for _ in range(len_t1+1)]

        for i in range(1, len_t1+1):
            for j in range(1, len_t2+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[len_t1][len_t2]

if __name__ == '__main__':
    solution = Solution()
    text1 = "abcde"
    text2 = "ace"
    print(solution.longestCommonSubsequence(text1, text2))
