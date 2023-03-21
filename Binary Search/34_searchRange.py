# -*- coding: utf-8 -*- #
# Name        : 34_searchRange.py
# Author      : shenchenlove 
# Time        : 2023/3/21 22:06
# Description : 34. 在排序数组中查找元素的第一个和最后一个位置

from typing import *

def lower_bound(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1 # 闭区间 [left, right]
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1 # 范围缩小到 [mid+1, right]
        else:
            right = mid - 1 # 范围缩小到 [left, mid-1]
    return left


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = lower_bound(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        end = lower_bound(nums, target + 1) -1 # 转换为找target+1,然后减1即为target  如果 start 存在，那么 end 必定存在
        return [start, end]


if __name__ == '__main__':
    solution = Solution()
    nums = [5,7,7,8,8,10]
    target = 8
    print(solution.searchRange(nums, target))
