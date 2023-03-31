# -*- coding: utf-8 -*- #
# Name        : 547_findCircleNum.py
# Author      : haishen yao
# Time        : 2023/3/31 15:55
# Description : 547. 省份数量
from typing import *

def dfs(i, isConnected, visited):
    for j in range(len(isConnected)):
        if isConnected[i][j] == 1 and j not in visited:
            visited.add(j)
            dfs(j, isConnected, visited)

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        res = 0
        nums = len(isConnected)
        visited = set() #记录城市是否已经被遍历
        for i in range(nums):
            if i not in visited:
                res += 1
                dfs(i, isConnected, visited)
        return res


if __name__ == '__main__':
    solution = Solution()
    isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(solution.findCircleNum(isConnected))