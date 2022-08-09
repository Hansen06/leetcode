# -*- coding: utf-8 -*-#
# Name:         88_merge
# Author:       shenchenlove
# Date:         2022/8/2 21:50
# Description:  88. 合并两个有序数组 https://leetcode.cn/problems/merge-sorted-array/

from typing import *

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        使用双指针方法，将两个数组看作队列，每次从两个数组头部取出比较小的数字放到结果中
        时间负责度O(m+n)
        """
        tp = []
        p0 = 0
        p1 = 0
        while p0 < m or p1 < n:
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
        nums1[:] = tp


if __name__ == '__main__':
    solution = Solution()

    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    solution.merge(nums1, m, nums2, n)
    print(nums1)
