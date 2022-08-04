# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  File Name：   704
  Description : 二分查找
  Author :    Hansen06
  date：     2022/2/25 13:49
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        first_idx = 0
        last_idx = length - 1
        while (first_idx <= last_idx):
            mid = first_idx + (last_idx - first_idx) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                first_idx = mid + 1
            elif nums[mid] > target:
                last_idx = mid - 1
        return -1


if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    solution = Solution()
    print(solution.search(nums, target))
