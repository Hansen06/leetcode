# -*- coding: utf-8 -*- #
# Name        : 142_detectCycle.py
# Author      : shenchenlove 
# Time        : 2023/3/4 22:22
# Description : 142 环形链表 II https://leetcode.cn/problems/linked-list-cycle-ii/solution/linked-list-cycle-ii-kuai-man-zhi-zhen-shuang-zhi-/

from typing import *
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        链表找环路的问题，有一个通用的解法——快慢指针, 每次 fast 前进两步， slow 前进一步
        :param head:
        :return:
        '''
        fast = head
        slow = head
        while True:
            if not (fast and fast.next):
                return
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast


if __name__ == '__main__':
    solution = Solution()
