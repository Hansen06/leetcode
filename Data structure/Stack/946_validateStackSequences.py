# -*- coding: utf-8 -*- #
# Name        : 946_validateStackSequences.py
# Author      : shenchenlove 
# Time        : 2023/5/25 21:23
# Description : 946. 验证栈序列

from typing import *
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if len(pushed) != len(popped):
            return False
        tmp = []
        j = 0
        for i in pushed:
            tmp.append(i)
            while tmp and tmp[-1] == popped[j]:
                tmp.pop()
                j += 1
        return len(tmp) == 0

if __name__ == '__main__':
    solution = Solution()
    pushed = [1,2,3,4,5]
    popped = [4,5,3,2,1]
    print(solution.validateStackSequences(pushed, popped))