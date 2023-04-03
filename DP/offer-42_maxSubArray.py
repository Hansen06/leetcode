# -*- coding: utf-8 -*- #
# Name        : offer-42_maxSubArray.py
# Author      : haishen yao
# Time        : 2023/4/1 23:02
# Description : 剑指 Offer 42. 连续子数组的最大和
from typing import *

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max = nums[0]
        sum = nums[0]
        for i in range(1, len(nums)):
            if sum >= 0:
                sum += nums[i]
            else:
                sum = nums[i]
            if sum > max:
                max = sum
        return max


if __name__ == '__main__':
    solution = Solution()
    nums = [1,2]
    print(solution.maxSubArray(nums))
