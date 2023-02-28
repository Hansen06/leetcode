# -*- coding: utf-8 -*- #
# Name        : 452_findMinArrowShots.py
# Author      : haishen yao
# Time        : 2023/2/28 17:48
# Description : 452 用最少数量的箭引爆气球

from typing import *

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        '''
        当前气球的左边界大于 标志位右边界时，需要多一只箭
        :param points:
        :return:
        '''
        if len(points) < 1:
            return 0
        points.sort(key=lambda x:x[1])

        small = 1
        le = len(points)
        pre_poi = points[0]
        for i in range(1, le):
            if pre_poi[1] < points[i][0]:
                small += 1
                pre_poi = points[i]

        return small


if __name__ == '__main__':
    solution = Solution()
    points = [[10, 16], [2, 8], [1, 6], [7, 12]]
    print(solution.findMinArrowShots(points))