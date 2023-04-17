# -*- coding: utf-8 -*- #
# Name        : 83_deleteDuplicates.py
# Author      : shenchenlove 
# Time        : 2023/4/17 21:50
# Description : 83. 删除排序链表中的重复元素

from typing import *
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        双指针解决
        :param head:
        :return:
        '''
        if not head:
            return

        slow = head
        fast = slow.next
        while fast:
            if slow.val == fast.val:
                fast = fast.next  # 重复时移动快指针
            else:
                slow.next = fast  # 不重复时将slow指向fast
                slow = slow.next  # 将slow移动到fast后面的一个元素上

        slow.next = fast #当重复元素在末尾时fast会一直走到空此时可以解决
        return head
