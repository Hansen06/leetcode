# -*- coding: utf-8 -*- #
# Name        : offer-63_maxProfit.py
# Author      : haishen yao
# Time        : 2023/4/1 23:18
# Description : 剑指 Offer 63. 股票的最大利润

from typing import *
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        small = float('+inf')
        for price in prices:
            small = min(small, price)
            profit = max(profit, price-small)
        return profit
