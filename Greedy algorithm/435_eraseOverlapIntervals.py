# -*- coding: utf-8 -*- #
# Name        : 435_eraseOverlapIntervals.py
# Author      : shenchenlove 
# Time        : 2023/2/22 22:59
# Description : 435. 无重叠区间

from typing import *
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        贪心策略为，优先保留结尾小且不相交的区间,先把区间按照结尾大小进行排序，然后选择结尾最小且和前一个区间不重叠的区间
        :param intervals:
        :return:
        '''
        if len(intervals) < 1:
            return 0

        intervals.sort(key = lambda x:x[1])
        n = len(intervals)
        right = intervals[0][1]
        remove = 0

        for i in range(1, n):
            if intervals[i][0] < right:
                remove += 1
            else:
                right = intervals[i][1]
        return  remove








if __name__ == '__main__':
    solution = Solution()
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    print(solution.eraseOverlapIntervals(intervals))
