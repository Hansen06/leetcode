# -*- coding: utf-8 -*- #
# Name        : offer-41_MovingAverage.py
# Author      : haishen yao
# Time        : 2023/4/5 12:17
# Description : 剑指 Offer II 041. 滑动窗口的平均值
import collections


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.sum = 0
        self.deque = collections.deque()


    def next(self, val: int) -> float:
        if len(self.deque) == self.size:
            self.sum -= self.deque.popleft()
        self.sum += val
        self.deque.append(val)
        return self.sum/len(self.deque)