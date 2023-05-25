# -*- coding: utf-8 -*- #
# Name        : 438_findAnagrams.py
# Author      : shenchenlove 
# Time        : 2023/5/24 21:36
# Description : 438. 找到字符串中所有字母异位词

from typing import *


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        '''
        滑动窗口+桶思想+ascii码
        :param s:
        :param p:
        :return:
        '''
        if len(s) < len(p):
            return []
        k = len(p)
        res = []
        s_count = [0] * 26
        p_count = [0] * 26
        for i in range(k):
            s_count[ord(s[i]) - 97] += 1
            p_count[ord(p[i]) - 97] += 1

        if s_count == p_count:
            res.append(0)

        slow = 1
        fast = k
        while fast < len(s):
            s_count[ord(s[slow - 1]) - 97] -= 1
            s_count[ord(s[fast]) - 97] += 1
            if s_count == p_count:
                res.append(slow)
            slow += 1
            fast += 1
        return res


if __name__ == '__main__':
    solution = Solution()
    s = 'aaa'
    p = 'aa'
    print(solution.findAnagrams(s, p))
