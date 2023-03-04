# -*- coding: utf-8 -*- #
# Name        : 665_checkPossibility.py
# Author      : haishen yao
# Time        : 2023/3/1 10:45
# Description : 665 非递减数列

from typing import *

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        '''
        贪心的策略，在遍历时，每次需要看连续的三个元素，也就是瞻前顾后,遵循以下两个原则：
            1. 需要尽可能不放大nums[i + 1]，这样会让后续非递减更困难；
            2. 如果缩小nums[i]，但不破坏前面的子序列的非递减性；
            修改方案1：将nums[i]缩小至nums[i + 1]；
            修改方案2：将nums[i + 1]放大至nums[i]；
        :param nums:
        :return:
        '''
        le = len(nums)
        if le <= 1:
            return True
        flag = True if nums[0] <= nums[1] else False
        for i in range(1, le-1):
            if nums[i] > nums[i+1]:
                if flag:
                    if nums[i+1] >= nums[i-1]:
                        nums[i] = nums[i+1]
                    else:
                        nums[i+1] = nums[i]
                    flag = False
                else:
                    return False
        return True



if __name__ == '__main__':
    solution = Solution()
    nums = [4, 2, 3]
    nums = [3,4,2,3]
    # nums = [4,2,1]
    print(solution.checkPossibility(nums))