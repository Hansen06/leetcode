# -*- coding: utf-8 -*-#
# Name:         455_findContentChildren
# Author:       shenchenlove
# Date:         2023/2/22 21:43
# Description:  455. 分发饼干 https://leetcode.cn/problems/assign-cookies/

from typing import *

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        '''
        贪心策略是，给剩余孩子里最小饥饿度的孩子分配最小的能饱腹的饼干
        :param g:
        :param s:
        :return:
        '''
        g.sort()
        s.sort()
        child = 0
        cookies = 0
        g_len = 0
        s_len = 0
        while child < g_len and cookies < s_len:
            if g[child] <= s[cookies]:
                child += 1
            cookies += 1
        return child


if __name__ == '__main__':
    solution = Solution()
    g = [1, 2]
    s = [1, 2, 3]
    print(solution.findContentChildren(g,s))
