# -*- coding: utf-8 -*- #
# Name        : offer-40_getLeastNumbers.py
# Author      : haishen yao
# Time        : 2023/3/28 11:25
# Description : 剑指 Offer 40. 最小的k个数

from typing import *

def exchange(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def quick_sort(arr, start, end):
    if start >= end:
        return
    mid = partition(arr, start, end)
    quick_sort(arr, start, mid-1)
    quick_sort(arr, mid+1, end)

def partition(arr, start, end):
    pivot = arr[start]
    left = start + 1
    right = end
    while left < right:
        while left < right and pivot >= arr[left]:
            left += 1
        while left < right and pivot <= arr[right]:
            right -= 1
        if left < right:
            exchange(arr, left, right)
            left += 1
            right -= 1

    if left == right and pivot < arr[right]:
        right -= 1
    exchange(arr, start, right)
    return right

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        quick_sort(arr, 0, len(arr)-1)
        return arr[:k]

if __name__ == '__main__':
    solution = Solution()
    arr = [3, 6, 1]
    k = 2
    print(solution.getLeastNumbers(arr, k))

