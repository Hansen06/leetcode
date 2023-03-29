# -*- coding: utf-8 -*- #
# Name        : 347_topKFrequent.py
# Author      : haishen yao
# Time        : 2023/3/29 10:22
# Description : 347. 前 K 个高频元素

from typing import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for num in nums:
            if map.get(num) is not None:
                map[num] += 1
            else:
                map[num] = 1
        _map = sorted(map.items(), key=lambda x:x[1], reverse=True)
        print(_map)

        return [_map[i][0] for i in range(k)]

if __name__ == '__main__':
    solution = Solution()
    nums = [3,0,1,0]
    k = 1
    print(solution.topKFrequent(nums, k))
