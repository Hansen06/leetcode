# -*- coding: utf-8 -*- #
# Name        : 82_deleteDuplicates.py
# Author      : shenchenlove 
# Time        : 2023/4/17 21:52
# Description : 82. 删除排序链表中的重复元素 II

from typing import *
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        dummynode = ListNode(0)
        dummynode.next = head
        slow = dummynode
        fast = slow.next

        while fast:
            flag = False
            while fast.next and fast.val == fast.next.val:
                fast = fast.next
                flag = True
            if not flag:
                slow.next = fast
                slow = slow.next
            fast = fast.next  # 不相等，fast自动往后移动一个位置

        slow.next = fast
        return dummynode.next

