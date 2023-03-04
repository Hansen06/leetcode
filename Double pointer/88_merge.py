# -*- coding: utf-8 -*- #
# Name        : 88_merge.py
# Author      : shenchenlove 
# Time        : 2023/3/4 21:41
# Description : 88 合并两个有序数组

from typing import *


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        从后往前循环
        """
        idx = m + n - 1
        idx1 = m - 1
        idx2 = n - 1
        while idx1 >= 0 or idx2 >= 0:
            if idx1 < 0:
                nums1[:idx + 1] = nums2[:idx2+1]
                break
            elif idx2 < 0:
                nums1[:idx + 1] = nums1[:idx1+1]
                break
            elif nums1[idx1] >= nums2[idx2]:
                nums1[idx] = nums1[idx1]
                idx -= 1
                idx1 -= 1
            elif nums1[idx1] < nums2[idx2]:
                nums1[idx] = nums2[idx2]
                idx -= 1
                idx2 -= 1

        return nums1


if __name__ == '__main__':
    solution = Solution()
    nums1 = [1,2,3,4,0,0]
    m = 4
    nums2 = [1,2]
    n = 2
    print(solution.merge(nums1, m, nums2, n))
