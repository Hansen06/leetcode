# -*- coding: utf-8 -*- #
# Name        : 167_twoSum.py
# Author      : shenchenlove 
# Time        : 2023/3/4 21:25
# Description : 167 两数之和 II - 输入有序数组

from typing import *

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        1、双指针
        :param numbers:
        :param target:
        :return:
        '''
        le = len(numbers)
        first = 0
        last = le-1
        while first <= last:
            if numbers[first] + numbers[last] < target:
                first += 1
            elif numbers[first] + numbers[last] > target:
                last -= 1
            elif numbers[first] + numbers[last] == target:
                return [first+1, last+1]

        return []



if __name__ == '__main__':
    solution = Solution()
    numbers = [2, 7, 11, 15]
    target = 9
    print(solution.twoSum(numbers, target))