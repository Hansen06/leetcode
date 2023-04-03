# -*- coding: utf-8 -*- #
# Name        : offer-52_getIntersectionNode.py
# Author      : haishen yao
# Time        : 2023/4/3 22:12
# Description : 剑指 Offer 52. 两个链表的第一个公共节点


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        node1 = headA
        node2 = headB
        while node1 != node2:
            if node1 is not None:
                node1 = node1.next
            else:
                node1 = headB
            if node2 is not None:
                node2 = node2.next
            else:
                node2 = headA

        return node1
