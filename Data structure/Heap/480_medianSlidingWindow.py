# -*- coding: utf-8 -*- #
# Name        : 480_medianSlidingWindow.py
# Author      : haishen yao
# Time        : 2023/4/5 21:02
# Description : 480. 滑动窗口中位数

from typing import *
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        med = []
        slow = 0
        fast = k
        length = len(nums)
        mid = k // 2
        while fast <= length:
            cur = nums[slow:fast]
            cur.sort()
            print(cur)
            if k % 2 == 0:
                med.append((cur[mid]+cur[mid-1])/2)
            else:
                med.append(cur[mid])
            slow += 1
            fast += 1
        return med


if __name__ == '__main__':
    solution = Solution()
    nums = [1,4,2,3,5,6]
    k = 4
    print(solution.medianSlidingWindow(nums, k))
