# -*- coding: utf-8 -*- #
# Name        : 219_containsNearbyDuplicate.py
# Author      : haishen yao
# Time        : 2023/4/8 18:44
# Description : 219. 存在重复元素 II
from typing import *
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map = {}
        length = len(nums)
        for i in range(length):
            if map.get(nums[i]) is not None:
                if abs(i-map[nums[i]]) <= k:
                    return True
                else:
                    map[nums[i]] = i
            else:
                map[nums[i]] = i

        return False

if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3, 1]
    k = 3
    print(solution.containsNearbyDuplicate(nums, k))
