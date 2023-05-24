# -*- coding: utf-8 -*- #
# Name        : 438_findAnagrams.py
# Author      : shenchenlove 
# Time        : 2023/5/24 21:36
# Description : 438. 找到字符串中所有字母异位词

from typing import *
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        k = len(p)
        p2n = {}
        for i in p:
            if p2n.get(i) is not None:
                p2n[i] += 1
            else:
                p2n[i] = 1
        slow = 0
        fast = k
        res = []
        flag = 0
        while fast <= len(s):
            k2n = {}
            for i in s[slow:fast]:
                if k2n.get(i) is not None:
                    k2n[i] += 1
                else:
                    k2n[i] = 1
            for k, v in p2n.items():
                if k2n.get(k) != v:
                    flag = 1
                    break

            if flag != 1:
                res.append(slow)
            slow += 1
            fast += 1
            flag = 0
        return res

if __name__ == '__main__':
    solution = Solution()
    s = 'aaa'
    b = 'aa'
    print(solution.findAnagrams(s, p))