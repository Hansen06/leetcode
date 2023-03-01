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

                last_poi = new_th[-1]
                le_new = len(new_th)
                n_min = last_poi[0]
                n_max = last_poi[1]
                record = [last_poi] #记录需要再次合并的区间
                for j in range(le_new-2,-1,-1): #从后往前循环
                    if last_poi[0] < new_th[j][1]:
                        record.append(new_th[j])

                for k in record:
                    new_th.remove(k)
                    n_min = n_min if n_min <= k[0] else k[0]
                    n_max = n_max if n_max >= k[1] else k[1]
                new_th.append([n_min, n_max])
            else:
                min = min if min <= points[i][0] else points[i][0]
                max = max if max >= points[i][1] else points[i][1]

            if i == le-1:
                min = min if min <= points[i][0] else points[i][0]
                max = max if max >= points[i][1] else points[i][1]
                new_th.append([min, max])

        ###需要考虑最后不能合并的情况
        print(new_th)
        last_poi = new_th[-1]
        le_new = len(new_th)
        n_min = last_poi[0]
        n_max = last_poi[1]
        record = [last_poi]
        for j in range(le_new - 2, -1, -1):
            if last_poi[0] < new_th[j][1]:
                record.append(new_th[j])

        for k in record:
            new_th.remove(k)
            n_min = n_min if n_min <= k[0] else k[0]
            n_max = n_max if n_max >= k[1] else k[1]
        new_th.append([n_min, n_max])

        print(new_th)

        return [x[1]-x[0]+1 for x in new_th]


if __name__ == '__main__':
    solution = Solution()
    s = "ababcbacadefegdehijhklij"
    print(solution.partitionLabels(s))