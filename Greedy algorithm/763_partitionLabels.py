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
        print(points)

        new_th = []
        pre_poi = points[0]
        le = len(points)
        min = pre_poi[0]
        max = pre_poi[1]
        for i in range(1, le):
            if points[i][0] > pre_poi[1]:
                pre_poi = points[i]
                new_th.append([min, max])
                min = pre_poi[0]
                max = pre_poi[1]
            else:
                min = min if min <= points[i][0] else points[i][0]
                max = max if max >= points[i][1] else points[i][1]
            if i == le-1:
                min = min if min <= points[i][0] else points[i][0]
                max = max if max >= points[i][1] else points[i][1]
                new_th.append([min, max])

        print(new_th)
        new_th.sort(key=lambda x:x[1])
        pre_poi = new_th[0]
        le = len(new_th)
        min = pre_poi[0]
        max = pre_poi[1]
        final_th = []
        for i in range(1, le):
            if new_th[i][0] > pre_poi[1]:
                pre_poi = new_th[i]
                final_th.append([min, max])
                min = pre_poi[0]
                max = pre_poi[1]
            else:
                min = min if min <= new_th[i][0] else new_th[i][0]
                max = max if max >= new_th[i][1] else new_th[i][1]
            if i == le-1:
                min = min if min <= new_th[i][0] else new_th[i][0]
                max = max if max >= new_th[i][1] else new_th[i][1]
                final_th.append([min, max])

        print(final_th)

        return [x[1]-x[0]+1 for x in final_th]



if __name__ == '__main__':
    solution = Solution()
    s = "ababcbacadefegdehijhklij"
    print(solution.partitionLabels(s))