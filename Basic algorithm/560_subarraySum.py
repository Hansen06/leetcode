# -*- coding: utf-8 -*- #
# Name        : 560_subarraySum.py
# Author      : haishen yao
# Time        : 2023/5/29 11:20
# Description : 560. 和为 K 的子数组

from typing import *
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        length = len(nums)
        prefixsum = [0] * length
        sums = 0
        for i in range(length):
            sums += nums[i]
            prefixsum[i] = sums

        map = {}
        map[0] = 1
        res = 0
        for i in range(length):
            target = prefixsum[i] - k
            res += map.get(target, 0)
            map[prefixsum[i]] = map.get(prefixsum[i], 0) + 1
        print(map)
        return res

if __name__ == '__main__':
    solution = Solution()
    nums = [1, 1, 1]
    k = 2
    print(solution.subarraySum(nums, k))