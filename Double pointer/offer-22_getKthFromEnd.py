# -*- coding: utf-8 -*- #
# Name        : offer-22_getKthFromEnd.py
# Author      : haishen yao
# Time        : 2023/4/3 22:01
# Description : 剑指 Offer 22. 链表中倒数第k个节点

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        slow = head
        fast = head
        for i in range(k):
            fast = fast.next

        while True:
            if fast is None:
                return slow
            fast = fast.next
