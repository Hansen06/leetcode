# -*- coding: utf-8 -*- #
# Name        : 122_maxProfit.py
# Author      : shenchenlove 
# Time        : 2023/2/28 23:16
# Description : 122 买卖股票的最佳时机 II

from typing import *

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        贪心的角度考虑我们每次选择贡献大于0的区间即能使得答案最大化

        :param prices:
        :return:
        '''
        ans = 0
        le = len(prices)
        for i in range(1, le):
            ans += max(0, prices[i] - prices[i-1])
        return ans

if __name__ == '__main__':
    solution = Solution()
    prices = [7,1,5,3,6,4]
    print(solution.maxProfit(prices))
