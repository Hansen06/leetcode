# -*- coding: utf-8 -*- #
# Name        : 220_containsNearbyAlmostDuplicate.py
# Author      : haishen yao
# Time        : 2023/4/8 18:55
# Description : 220. 存在重复元素 III
from typing import *


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        '''
        利用桶思想 https://leetcode.cn/problems/contains-duplicate-iii/solution/gua-he-xin-shou-peng-you-de-shi-pin-ti-j-c4ua/
        :param nums:
        :param indexDiff:
        :param valueDiff:
        :return:
        '''
        bucket = {}
        bucket_size = valueDiff + 1
        length = len(nums)
        for i in range(length):
            bucket_id = nums[i] // bucket_size  # 求得桶号

            if bucket_id in bucket and i - bucket[bucket_id] <= indexDiff:
                return True

            bucket[bucket_id] = i # 桶里放的是当前数的index

            if bucket_id - 1 in bucket and abs(nums[bucket[bucket_id - 1]] - nums[i]) <= valueDiff \
                    and i - bucket[bucket_id - 1] <= indexDiff:
                return True

            if bucket_id + 1 in bucket and abs(nums[bucket[bucket_id + 1]] - nums[i]) <= valueDiff \
                    and i - bucket[bucket_id + 1] <= indexDiff:
                return True

        return False

if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3, 1]
    k = 3
    t = 0
    print(solution.containsNearbyAlmostDuplicate(nums, k, t))
