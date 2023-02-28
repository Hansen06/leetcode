# -*- coding: utf-8 -*- #
# Name        : 763_partitionLabels.py
# Author      : haishen yao
# Time        : 2023/2/28 18:35
# Description : 763 划分字母区间

from typing import *

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        '''
        先统计每个字符出现的首尾，然后进行最大串联，能连在一起的都连在一起，不想交的则分割，统计分割的个数
        :param s:
        :return:
        '''
        points = []
        sets = set(s)
        for i in sets:
            points.append([s.find(i),s.rfind(i)])

        points.sort(key=lambda x:x[1])







if __name__ == '__main__':
    solution = Solution()