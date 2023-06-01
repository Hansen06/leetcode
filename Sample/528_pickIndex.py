# -*- coding: utf-8 -*- #
# Name        : 528_pickIndex.py
# Author      : haishen yao
# Time        : 2023/6/1 11:23
# Description : 528. 按权重随机选择
import random
from typing import *


class Solution:

    def __init__(self, w: List[int]):
        self.sum = 0
        self.presum = [0] * len(w)
        for i in range(len(w)):
            self.sum += w[i]
            self.presum[i] = self.sum

    def pickIndex(self) -> int:
        x = random.randint(1, self.sum)

        left = 0
        right = len(self.presum) - 1
        while left < right:
            mid = (left + right) // 2
            if x <= self.presum[mid]:
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    w = [1, 2, 3]
    solution = Solution(w)
    param_1 = solution.pickIndex()
    print(param_1)
