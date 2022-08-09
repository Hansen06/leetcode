# -*- coding: utf-8 -*-#
# Name:         3_lengthOfLongestSubstring
# Author:       shenchenlove
# Date:         2022/7/25 20:27
# Description:  3. 无重复字符的最长子串 https://leetcode.cn/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        最简单粗暴地方法，循环
        两个indx记录首尾
        注意边界，为空的时候
        '''
        max = 0
        if len(s) < 1:
            return 0
        for idx,i in enumerate(s):
            cur = [i]
            for j in s[idx+1:]:
                if j not in cur:
                    cur.append(j)
                    max = max if max > len(cur) else len(cur)
                else:
                    break

        max = max if max > 1 else 1 # 全部相同地情况
        return max

    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        滑动窗口
        '''
        first_idx = 0
        if len(s) < 1:
            return 0

        set_ = set()
        cur_len = 0
        max = 0
        for idx in range(len(s)):
            cur_len += 1
            while s[idx] in set_:
                cur_len -= 1
                set_.remove(s[first_idx])
                first_idx += 1

            max = max if max > cur_len else cur_len
            set_.add(s[idx] )

        return max


if __name__ == '__main__':
    solution = Solution()

    s = "abcabcbb"
    # s = "bbbbb"
    # s = "pwwkew"
    print(solution.lengthOfLongestSubstring(s))
