# -*- coding: utf-8 -*- #
# Name        : 300_lengthOfLIS.py
# Author      : haishen yao
# Time        : 2023/4/5 16:59
# Description : 300. 最长递增子序列

from typing import *

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        动态规划，状态方程dp[i] = max(dp[i], dp[j]+1) for j in [0,i)
        :param nums:
        :return:
        '''
        length = len(nums)
        dp = [1] * length
        for i in range(length):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)

    def lengthOfLIS1(self, nums: List[int]) -> int:
        '''
        动态规划+二分查找 讲解 https://leetcode.cn/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-dong-tai-gui-hua-2/
        :param nums:
        :return:
        '''
        length = len(nums)
        tails = [0] * length #维护一个递增序列
        len_tails = 0 #tails 当前长度
        for num in nums:
            left = 0
            right = len_tails
            while left < right:
                mid = (left + right)//2
                if tails[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            tails[left] = num
            if right == len_tails:
                len_tails += 1
        return len_tails

if __name__ == '__main__':
    solution = Solution()
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(solution.lengthOfLIS1(nums))