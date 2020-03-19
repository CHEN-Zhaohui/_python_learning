# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:21:50 2020

@author: Chen Zhaohui
"""
class Solution:
    def length_longest_substring_1(self, s: str) ->int:
        if s == '':
            print(0)
        if len(s) == 1:
            print(1)
        def find_left_longest(s, i):
            tmp_str = s[i]
            j = i-1
            while j >= 0 and s[j] not in tmp_str:
                tmp_str += s[j]
                j -= 1
            return len(tmp_str)
        length = 0
        for i in range(len(s)):
            length = max(length, find_left_longest(s, i))
        return length

    def length_longest_substring_2(self, s:str):
        length = 0
        for i in range(len(s)-1):
            max_arr = []
            for j in range(i, len(s)):
                if s[j] not in max_arr:
                    max_arr.append(s[j])
                else:
                    break
            tmp_length = len(max_arr)
            if tmp_length > length:
                length = tmp_length
        return length

    def length_longest_substring_3(self, s:str):
        length, j = 0, -1
        for i, x in enumerate(s):
            if x in s[j + 1:i]:
                length = max(length, i - j - 1)
                j = s[j + 1:i].index(x) + j + 1
        return max(length, len(s) - 1 - j)


if __name__ == '__main__':
    s = "pwwkew"
    test = Solution()
    print(test.length_longest_substring_3(s))

