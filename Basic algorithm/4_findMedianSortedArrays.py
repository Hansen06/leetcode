# -*- coding: utf-8 -*-#
# Name:         4_findMedianSortedArrays
# Author:       shenchenlove
# Date:         2022/8/2 22:05
# Description:  4. 寻找两个正序数组的中位数 https://leetcode.cn/problems/median-of-two-sorted-arrays/

from typing import *

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        tp = []
        p0 = 0
        p1 = 0
        m = len(nums1)
        n = len(nums2)
        while p0 < len(nums1) or p1 < len(nums2):
            if p0 == m:
                tp.append(nums2[p1])
                p1 += 1
            elif p1 == n:
                tp.append(nums1[p0])
                p0 += 1
            elif nums1[p0] <= nums2[p1]:
                tp.append(nums1[p0])
                p0 += 1
            else:
                tp.append(nums2[p1])
                p1 += 1
        if len(tp) % 2 != 0:
            return tp[int(len(tp)/2)]
        else:
            return (tp[int(len(tp)/2)-1] + tp[int(len(tp)/2)])/2

if __name__ == '__main__':
    solution = Solution()
    nums1 = [1, 3]
    nums2 = [2]
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(solution.findMedianSortedArrays(nums1, nums2))
