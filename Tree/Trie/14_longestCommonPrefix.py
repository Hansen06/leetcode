# -*- coding: utf-8 -*- #
# Name        : 14_longestCommonPrefix.py
# Author      : haishen yao
# Time        : 2023/4/4 11:27
# Description : 14. 最长公共前缀

from typing import *
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) < 1:
            return ''
        prefix = strs[0]
        for i in range(1, len(strs)):
            index = 0
            cur_len = min(len(prefix), len(strs[i]))
            while index < cur_len and prefix[index] == strs[i][index]:
                index += 1
            prefix = strs[i][:index]
            if len(prefix) < 1:
                break

        return prefix

if __name__ == '__main__':
    solution = Solution()
    strs = ["flower","flow","flight"]
    print(solution.longestCommonPrefix(strs))

