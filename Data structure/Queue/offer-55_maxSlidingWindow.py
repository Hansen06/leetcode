# -*- coding: utf-8 -*- #
# Name        : offer-55_maxSlidingWindow.py
# Author      : haishen yao
# Time        : 2023/4/5 11:25
# Description : 剑指 Offer 59 - I. 滑动窗口的最大值
import collections
from typing import *

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        时间负责度 O(n*k)
        :param nums:
        :param k:
        :return:
        '''
        res = []
        slow = 0
        fast = k
        length = len(nums)
        while fast <= length:
            res.append(max(nums[slow:fast]))
            fast += 1
            slow += 1
        return res

    def maxSlidingWindow1(self, nums: List[int], k: int) -> List[int]:
        '''
        使用队列
        时间负责度 O(n*1)
        :param nums:
        :param k:
        :return:
        '''
        deque = collections.deque()
        for i in range(k):
            while deque and nums[deque[-1]] < nums[i]:
                deque.pop()
            deque.append(i)
        res = [nums[deque[0]]]
        for i in range(k, len(nums)):
            if deque[0] == i-k: #队列最右端不在当前窗口，则移出
                deque.popleft()
            while deque and nums[deque[-1]] < nums[i]: #从队列右侧判断当前值是否大于队列中的值，大于则将队列中的数移出
                deque.pop()
            deque.append(i) #将当前值index放入队列右侧
            res.append(nums[deque[0]])
        return res




if __name__ == '__main__':
    solution = Solution()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(solution.maxSlidingWindow1(nums, k))