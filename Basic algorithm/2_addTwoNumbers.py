# -*- coding: utf-8 -*-#
# Name:         2_addTwoNumbers
# Author:       shenchenlove
# Date:         2022/7/21 20:56
# Description:  2. 两数相加

from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        难点：链表的循环遍历
        思路：循环链表，从头依次相加，大于10进位1, 保持一个进位值
        '''
        head = point = ListNode(0)
        carry = 0

        while l1 or l2:
            if l1 != None and l2 != None:
                sum = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif l1 == None:
                sum = carry + l2.val
                l2 = l2.next
            else:
                sum = carry + l1.val
                l1 = l1.next

            carry = sum // 10
            val = sum % 10
            point.next = ListNode(val)
            point = point.next

        if carry != 0:
            new_point = ListNode(1)
            point.next = new_point

        return head.next


if __name__ == '__main__':
    solution = Solution()
    l1 = [2,4,3]
    l2 = [5,6,4]
    _l1 = point1 = ListNode(0)
    _l2 = point2 = ListNode(0)
    for idx, i in enumerate(l1):
        new_point = ListNode(i)
        point1.next = new_point
        if idx < len(l1):
            point1 = point1.next
    for idx, i in enumerate(l2):
        new_point = ListNode(i)
        point2.next = new_point
        if idx < len(l2):
            point2 = point2.next

    res = solution.addTwoNumbers(_l1, _l2)
    while res:
        print(res.val)
        res = res.next
