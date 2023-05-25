# -*- coding: utf-8 -*- #
# Name        : 1299_replaceElements.py
# Author      : shenchenlove 
# Time        : 2023/5/25 20:40
# Description : 1299. 将每个元素替换为右侧最大元素

from typing import *
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) < 1:
            return
        max = -1
        for i in range(len(arr)-1, -1, -1):
            tmp = arr[i]
            arr[i] = max
            if tmp > max:
                max = tmp
        return arr

if __name__ == '__main__':
    solution = Solution()
    arr = [17, 18, 5, 4, 6, 1]
    print(solution.replaceElements(arr))