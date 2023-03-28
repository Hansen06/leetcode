# -*- coding: utf-8 -*- #
# Name        : offer-40_getLeastNumbers.py
# Author      : haishen yao
# Time        : 2023/3/28 11:25
# Description : 剑指 Offer 40. 最小的k个数

from typing import *
def quick_sort(arr, left, right):
    '''
    快排 时间复杂度O(NlogN)
    :param arr:
    :param left:
    :param right:
    :return:
    '''
    if left >= right:
        return
    first = left
    last = right
    key = arr[first]
    while first < last:
        while first < last and key <= arr[last]:
            last -= 1
        arr[first] = arr[last]
        while first < last and key >= arr[first]:
            first += 1
        arr[last] = arr[first]

    arr[first] = key
    quick_sort(arr, left, first)
    quick_sort(arr, first+1, right)

def quick_sort(arr, left, right, k):
    '''
    时间复杂度O(N) N+N/2+N/4+...+N/N = (N-1/2)/(1-1/2) = 2N-1
    :param arr:
    :param left:
    :param right:
    :param k:
    :return:
    '''
    if k >= len(arr):
        return arr
    first = left
    last = right
    key = arr[first]
    while first < last:
        while first < last and key <= arr[last]:
            last -= 1
        arr[first] = arr[last]
        while first < last and key >= arr[first]:
            first += 1
        arr[last] = arr[first]
    arr[first] = key
    if k < first:
        quick_sort(arr, left, first, k)
    if k > first:
        quick_sort(arr, first+1, right, k)

    return arr[:k]



class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        # quick_sort(arr, 0, len(arr)-1)
        # print(arr)
        # return arr[:k]
        return quick_sort(arr, 0, len(arr)-1, k)

if __name__ == '__main__':
    solution = Solution()
    arr = [3, 2, 1]#[0,1,2,1]
    k = 2
    print(solution.getLeastNumbers(arr, k))

