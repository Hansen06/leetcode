# -*- coding: utf-8 -*- #
# Name        : 76_minWindow.py
# Author      : shenchenlove 
# Time        : 2023/3/5 20:13
# Description : 76 最小覆盖子串


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        滑动窗口， 维护一个计数器，该计数器记录当前窗口是否全部包含了t, 包含则-1，等于0时说明当前窗口刚好包含t
        :param s:
        :param t:
        :return:
        '''
        if len(t) > len(s):
            return ''

        need = len(t)
        map = {}
        for i in t:
            if map.get(i):
                map[i] += 1
            else:
                map[i] = 1

        n = len(s)
        left = right = 0
        min_len = n + 1
        start = 0
        end = -1

        for right in range(n):
            ch = s[right]
            if ch in map:
                if map[ch] > 0:  # 对当前字符ch还有需求
                    need -= 1  # 此时新加入窗口中的ch对need有影响
                map[ch] -= 1

            # 当 当前窗口包含s时，现在开始移动左侧指针，使得窗口最小
            while need == 0:  # need=0，当前窗口完全覆盖了t
                if right - left + 1 < min_len:  # 首先判断当前窗口大小是否小于之前满足条件的窗口的大小
                    min_len = right - left + 1
                    start = left
                    end = right

                # 移动左指针
                ch = s[left]  # 窗口中要滑出的字符
                if ch in map:
                    if map[ch] >= 0:  # 对当前字符ch还有需求，或刚好无需求(其实此时只有=0的情况)
                        need += 1
                    map[ch] += 1

                left += 1

        return s[start:end + 1]


if __name__ == '__main__':
    solution = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    print(solution.minWindow(s, t))
