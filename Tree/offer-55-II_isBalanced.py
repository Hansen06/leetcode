# -*- coding: utf-8 -*- #
# Name        : offer-55-II_isBalanced.py
# Author      : haishen yao
# Time        : 2023/4/5 22:15
# Description : 剑指 Offer 55 - II. 平衡二叉树
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        '''
        后续遍历
        当节点root 左 / 右子树的深度差 ≤ 1：则返回当前子树的深度，即节点 root 的左 / 右子树的深度最大值+1 （ max(left, right) + 1 ）；
        当节点root 左 / 右子树的深度差 >2 ：则返回−1 ，代表 此子树不是平衡树 。
        :param root:
        :return:
        '''
        def recur(root):
            if root is None:
                return 0
            left = recur(root.left)
            if left == -1:
                return -1
            right = recur(root.right)
            if right == -1:
                return -1
            return max(left, right) + 1  if abs(left-right) < 2 else -1
        return recur(root) != -1
