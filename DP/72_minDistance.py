#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# File         : 72_minDistance.py
# Author       : haishen.yao
# Time         : 2023/5/5 下午8:45
# Description  : 72. 编辑距离

from typing import *

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 or not word2:
            return max(len(word1), len(word2))

        m = len(word1) + 1
        n = len(word2) + 1
        dp = [[0]*n for _ in range(m)]
        print(dp)
        for i in range(0, m):
            for j in range(0, n):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                else:
                    dp[i][j] = min(
                        dp[i-1][j-1] + (0 if word1[i-1]==word2[j-1] else 1),
                        min(dp[i-1][j] + 1, dp[i][j-1] + 1)
                    )
        print(dp)
        return dp[m-1][n-1]

if __name__ == '__main__':
    solution = Solution()
    word1 = "a"
    word2 = "b"
    print(solution.minDistance(word1, word2))