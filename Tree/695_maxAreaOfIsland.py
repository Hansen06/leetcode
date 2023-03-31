# -*- coding: utf-8 -*- #
# Name        : 695_maxAreaOfIsland.py
# Author      : haishen yao
# Time        : 2023/3/31 15:31
# Description : 695. 岛屿的最大面积

from typing import *

def dfs(grid, r, c):
    if not (r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0])): #判断是否越界
        return 0
    if grid[r][c] != 1:
        return 0
    grid[r][c] = 2 #遍历过的不再遍历
    return 1 + dfs(grid, r-1, c) + dfs(grid, r+1, c) + dfs(grid, r, c-1) + dfs(grid, r, c+1)


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if len(grid) < 1:
            return 0
        res = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    size = dfs(grid, i, j)
                    res = max(res, size)
        return res


if __name__ == '__main__':
    solution = Solution()
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    grid = [[1]]
    print(solution.maxAreaOfIsland(grid))

