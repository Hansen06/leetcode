# -*- coding: utf-8 -*- #
# Name        : 81_search.py
# Author      : shenchenlove 
# Time        : 2023/3/24 21:59
# Description : 81. 搜索旋转排序数组 II

from typing import *
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # return target in nums
        if len(nums) < 1:
            return False

        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end)//2
            if nums[mid] == target:
                return True
            if nums[mid] == nums[start]: #第一种情况，start==mid
                start += 1
                continue
            if nums[mid] < nums[start]: #第二种情况，start > mid, 右侧有序
                if target > nums[mid] and target <= nums[end]: # 右侧有序不一定在右侧，有可能有一部更大的值在左侧
                    start = mid + 1
                else:
                    end = mid - 1
            else: #第三种情况，start < mid, 左侧有序
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
        return False

if __name__ == '__main__':
    solution = Solution()
    nums = [3, 1]
    target = 1
    print(solution.search(nums, target))
