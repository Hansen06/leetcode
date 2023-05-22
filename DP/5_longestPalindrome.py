# -*- coding: utf-8 -*- #
# Name        : 5_longestPalindrome.py
# Author      : haishen yao
# Time        : 2023/4/14 11:16
# Description : 5. 最长回文子串
from typing import *

class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        翻转使用最长公共子序列的思想解决
        :param s:
        :return:
        '''
        s2 = []
        for i in range(len(s)-1, -1, -1):
            s2.append(s[i])
        text1 = s
        text2 = ''.join(s2)

        len_t1 = len(text1)
        len_t2 = len(text2)
        dp = [[0] * (len_t2 + 1) for _ in range(len_t1 + 1)]

        res = []

        for i in range(1, len_t1 + 1):
            for j in range(1, len_t2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    res.append(text1[i-1])
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        print(res)
        return dp[len_t1][len_t2]


if __name__ == '__main__':
    solution = Solution()
    s = "babad"
    print(solution.longestPalindrome(s))
