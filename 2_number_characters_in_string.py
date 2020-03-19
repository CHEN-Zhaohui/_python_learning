# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:21:50 2020

@author: Chen Zhaohui
"""

def number_characters_in_string_1(str):
    str_array = [str[i] for i in range(len(str))]
    hashmap = {}
    for i, item in enumerate(str_array):
        hashmap[item] = i
    print(len(hashmap))

def number_characters_in_string_2(str):
    temp = [str[0]]
    for i in range(1, len(str)):
        if str[i] not in temp:
            temp.append(str[i])
    print(len(temp))



def main():
    str = "pwwkew"
    number_characters_in_string_2(str)


if __name__ == '__main__':
    main()

