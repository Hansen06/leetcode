# -*- coding: utf-8 -*- #
# Name        : 33_search.py
# Author      : shenchenlove 
# Time        : 2023/3/25 12:04
# Description : 33. 搜索旋转排序数组

from typing import *
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) < 1:
            return -1

        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end)//2
            if nums[mid] == target:
                return mid
            if nums[start] <= nums[mid]: # 左侧有序  这里注意等号
                if target < nums[mid] and target >= nums[start]:
                    end = mid - 1
                else:
                    start = mid + 1
            else: #右侧有序
                if target > nums[mid] and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1

if __name__ == '__main__':
    solution = Solution()
    nums = [3, 1]
    target = 1
    print(solution.search(nums, target))
