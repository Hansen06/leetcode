# -*- coding: utf-8 -*- #
# Name        : 215_findKthLargest.py
# Author      : shenchenlove 
# Time        : 2023/3/28 22:09
# Description : 215. 数组中的第K个最大元素

from typing import *

def partition(arr, left, right):
    key = arr[left]
    first = left
    last = right
    while first < last:
        while first < last and key <= arr[last]:
            last -= 1
        arr[first] = arr[last]
        while first < last and key >= arr[first]:
            first += 1
        arr[last] = arr[first]
    arr[first] = key
    return last

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left = 0
        right = len(nums) - 1
        target = len(nums) - k
        while True:
            mid = partition(nums, left, right)
            if mid == target:
                return nums[mid]
            elif mid < target:
                left = mid + 1
            else:
                right = mid - 1

if __name__ == '__main__':
    solution = Solution()
    nums = [2,1]
    k = 2
    print(solution.findKthLargest(nums,k))