# -*- coding: utf-8 -*- #
# Name        : 605_canPlaceFlowers.py
# Author      : shenchenlove 
# Time        : 2023/2/26 21:59
# Description : 605 种花问题

from typing import *

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        '''
        看连续的三个坑是否满足，为了避免两边的漏掉，在两边添加两个空坑
        :param flowerbed:
        :param n:
        :return:
        '''
        count = 0
        i = 1
        flowerbed = [0] + flowerbed + [0] #两边添加两个空坑
        le = len(flowerbed)
        while i < le-1:
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                count+=1
                i+=2
            else:
                i += 1
        if count >= n:
            return True
        return False

    def canPlaceFlowers_greedy(self, flowerbed: List[int], n: int) -> bool:
        '''
        看两个花中间进行计算，同事考虑开头和结尾的情况,可种的最多个数为(坑数+1)//2
        两个花之间最多可以种： 首先有j-i-1个坑，然后靠近1的不能种，再减去两个j-i-1-2, 剩j-i-3个坑，最多可以种 (j-i-3+1)//2=(j-i-2)//2 个花
        开头：i个坑，靠近1的不能种，剩i-1可种,最多可种 (i-1+1)//2=i//2
        结尾：m-i-1个坑，靠近1的不能种，剩m-i-1-1可种, 最多可种 (m-i-1-1+1)//2=(m-i-1)//2
        :param flowerbed:
        :param n:
        :return:
        '''
        count = 0
        le = len(flowerbed)
        pre = -1
        for i in range(le):
            if flowerbed[i] == 1:
                if pre < 0:
                    count += i//2
                else:
                    count += (i-pre-2)//2
                pre = i

        if pre < 0:
            count += (le+1)//2
        else:
            count += (le-pre-1)//2
        return count >= n

if __name__ == '__main__':
    solution = Solution()
    flowerbed = [1, 0, 0, 0, 1]
    n = 1
    print(solution.canPlaceFlowers(flowerbed, n))
    print(solution.canPlaceFlowers_greedy(flowerbed, n))