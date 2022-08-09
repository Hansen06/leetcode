# -*- coding: utf-8 -*-#
# Name:         1_twoSum
# Author:       shenchenlove
# Date:         2022/7/19 20:55
# Description:  1. 两数之和  https://leetcode.cn/problems/two-sum/

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        暴力查找，双层for循环
        时间O(n2)
        '''
        for s_idx, i in enumerate(nums):
            for e_idx, j in enumerate(nums[s_idx+1:]):
                if i + j == target:
                    return [s_idx, e_idx+s_idx+1]
        return

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        构建hash map，快速查找
        时间o(n)
        '''
        hash = {}
        for idx, i in enumerate(nums):
            hash[i] = idx

        for idx, j in enumerate(nums):
            if hash.get(target-j) is not None and hash.get(target-j) != idx:
                return [idx, hash.get(target-j)]
        return

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        优化掉了构建hash表的时间，不用单独构建hash表
        构建hash map，快速查找
        时间o(n)
        '''
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []




if __name__ == '__main__':
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    nums = [2, 5, 5, 11]
    target = 10
    nums = [3, 2, 4]
    target = 6
    print(solution.twoSum(nums, target))