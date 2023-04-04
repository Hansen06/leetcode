# -*- coding: utf-8 -*- #
# Name        : offer-65_minimumLengthEncoding.py
# Author      : haishen yao
# Time        : 2023/4/3 22:41
# Description : 剑指 Offer II 065. 最短的单词编码

import collections
from typing import *
from functools import reduce
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:

        res = set(words)
        for word in words:
            for j in range(1, len(word)):
                if word[j:] in res:
                    res.remove(word[j:])
        return sum([len(w) + 1 for w in res])

    def minimumLengthEncoding1(self, words: List[str]) -> int:
        '''
        trie树的方法
        :param words:
        :return:
        '''
        words = list(set(words))  # remove duplicates
        # Trie is a nested dictionary with nodes created
        # when fetched entries are missing

        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()

        # reduce(..., S, trie) is trie[S[0]][S[1]][S[2]][...][S[S.length - 1]]
        nodes = [reduce(dict.__getitem__, word[::-1], trie)
                 for word in words]

        # Add word to the answer if it's node has no neighbors
        return sum(len(word) + 1
                   for i, word in enumerate(words)
                   if len(nodes[i]) == 0)



if __name__ == '__main__':
    solution = Solution()
    words = ["time", "me", "bell"]
    print(solution.minimumLengthEncoding1(words)) # s = "time#bell#"
