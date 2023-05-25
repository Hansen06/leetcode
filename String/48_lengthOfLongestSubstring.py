# -*- coding: utf-8 -*- #
# Name        : 48_lengthOfLongestSubstring.py
# Author      : shenchenlove 
# Time        : 2023/5/25 21:54
# Description : 剑指 Offer 48. 最长不含重复字符的子字符串

from typing import *
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sets = set()
        first = 0
        max_len = 0
        cur_len = 0
        for i in range(len(s)):
            cur_len += 1
            while s[i] in sets:
                cur_len -= 1
                sets.remove(s[first])
                first += 1

            if cur_len > max_len:
                max_len = cur_len
            sets.add(s[i])
        return max_len

if __name__ == '__main__':
    solution = Solution()
    s = "qrsvbspk"
    print(solution.lengthOfLongestSubstring(s))