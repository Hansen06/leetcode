# -*- coding: utf-8 -*- #
# Name        : 1162_maxDistance.py
# Author      : haishen yao
# Time        : 2023/3/31 15:21
# Description : 1162. 地图分析

from typing import *

def inArea(grid, r, c) :
    return 0 <= r and r < len(grid)  and 0 <= c and c < len(grid)

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        N = len(grid)
        print(N)

        queue = []
        # 将所有的陆地格子加入队列
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:
                    queue.append((i, j))

        print(len(queue))
        # 如果地图上只有陆地或者海洋，返回 -1
        if len(queue) < 1 or len(queue) == N*N :
            return -1

        moves = [
            (-1, 0), (1, 0), (0, -1), (0, 1)
        ]

        distance = -1 # 记录当前遍历的层数（距离）
        while queue:
            distance+=1
            n = len(queue)
            for i in range(n):
                node = queue.pop(0)
                r = node[0]
                c = node[1]
                for move in moves:
                    r2 = r + move[0]
                    c2 = c + move[1]
                    if inArea(grid, r2, c2) and grid[r2][c2] == 0:
                        grid[r2][c2] = 2
                        queue.append((r2, c2))

        return distance

if __name__ == '__main__':
    solution = Solution()
    grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
    print(solution.maxDistance(grid))

