# -*- coding: utf-8 -*- #
# Name        : offer-55-I_maxDepth.py
# Author      : haishen yao
# Time        : 2023/4/5 22:02
# Description : 剑指 Offer 55 - I. 二叉树的深度

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        '''
        深度遍历
        :param root:
        :return:
        '''
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def maxDepth(self, root: TreeNode) -> int:
        '''
        层次遍历
        :param root:
        :return:
        '''
        if root is None:
            return 0
        queue = [root]
        depth = 0
        while queue:
            tmp = []
            for node in queue:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            queue = tmp
            depth += 1
        return depth



