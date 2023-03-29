# -*- coding: utf-8 -*- #
# Name        : quick_sort.py
# Author      : haishen yao
# Time        : 2023/3/29 10:37
# Description : 快排函数

def partition(arr, left, right):
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
    return last

def quick_sort(arr, left, right):
    if left >= right:
        return
    mid = partition(arr, left, right)
    quick_sort(arr, left, mid-1)
    quick_sort(arr, mid+1, right)
