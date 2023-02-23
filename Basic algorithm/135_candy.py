# -*- coding: utf-8 -*- #
# Name        : 135_candy.py
# Author      : shenchenlove 
# Time        : 2023/2/22 22:28
# Description : 135. 分发糖果 https://leetcode.cn/problems/candy/

from typing import *
class Solution:
    def candy(self, ratings: List[int]) -> int:
        '''
        贪心策略即为，在每次遍历中，只考虑并更新相邻一侧的大小关系
        :param ratings:
        :return:
        '''
        r_len = len(ratings)
        if r_len < 2:
            return r_len

        size = [1]*r_len
        for i in range(1, r_len):
            if ratings[i] > ratings[i-1]:
                size[i] = size[i-1] + 1

        for i in range(r_len-1, 0, -1):
            if ratings[i-1] > ratings[i]:
                size[i-1] = max(size[i] + 1, size[i-1]) # 糖果数原本就比右边多，就保持原来的数量即可

        return sum(size)

if __name__ == '__main__':
    solution = Solution()
    ratings = [1, 2, 2]
    ratings = [1, 0, 2]
    ratings = [1,3,2,2,1]
    ratings = [1,3,4,5,2]
    print(solution.candy(ratings))



