# -*- coding: utf-8 -*-#
# Name:         2_addTwoNumbers
# Author:       shenchenlove
# Date:         2022/7/21 20:56
# Description:  2. 两数相加 https://leetcode.cn/problems/add-two-numbers/

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

    def addTwoNumbers1(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        占用其中一个链表，节省空姐，并且如果一个为空后即结束循环
        :param l1:
        :param l2:
        :return:
        '''
        res = l1
        carry = 0
        # 死循环
        while True:
            # 计算本位和
            cur = l1.val + l2.val + carry
            if cur >= 10:
                carry = 1
                l1.val = cur - 10
            else:
                carry = 0
                l1.val = cur
            # 如果短指针的后继是空
            if l1.next is None:
                # 长指针后置
                l2 = l2.next
                # 短指针的后继长指针
                l1.next = l2
                # 退出
                break
            elif l2.next is None:
                break
            # 两指针后置
            l1, l2 = l1.next, l2.next
        # 当长指针不是空时
        while l1.next:
            l1 = l1.next
            # 计算本位
            cur = l1.val + carry
            # 计算进位
            carry = cur // 10
            # 更新本位
            l1.val = cur % 10
        # 如果进位大于0
        if carry > 0:
            # 生成一个新结点，其值是进位，将其加入长指针后
            l1.next = ListNode(carry)
        # 返回
        return res


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

    res = solution.addTwoNumbers1(_l1, _l2)
    while res:
        print(res.val)
        res = res.next
