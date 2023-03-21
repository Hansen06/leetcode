# -*- coding: utf-8 -*- #
# Name        : 69_mySqrt.py
# Author      : shenchenlove 
# Time        : 2023/3/21 21:59
# Description : 69. x 的平方根


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        l = 0
        r = x
        ans = -1
        while l <= r:
            mid = l + (r-l)//2
            # mid = (l + r) // 2
            if mid * mid <= x:
                l = mid + 1
                ans = mid
            else:
                r = mid - 1
        return ans

if __name__ == '__main__':
    solution = Solution()
    x = 4
    print(solution.mySqrt(x))
