# -*- coding: utf-8 -*- #
# Name        : 665_checkPossibility.py
# Author      : haishen yao
# Time        : 2023/3/1 10:45
# Description : 665 非递减数列

from typing import *

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        '''

        :param nums:
        :return:
        '''
        change = 0
        le = len(nums)
        for i in range(1, le):
            if nums[i] < nums[i-1]:
                if (i <= le-2 and nums[i+1]-nums[i-1] >= 1):
                    change += 1
        if change > 1:
            return False
        return True



if __name__ == '__main__':
    solution = Solution()
    nums = [4, 2, 3]
    print(solution.checkPossibility(nums))