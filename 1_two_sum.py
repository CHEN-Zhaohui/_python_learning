# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 14:06:02 2020

@author: Chen Zhaohui
"""
def two_sum_1(num, array):
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == num:
                print([i, j])
                break

def two_sum_2(num, array):
    """
    index() 函数用于从列表中找出某个值第一个匹配项的索引位置，用法：list.index(x[, start[, end]])。
    temp = [('a', 1, 1.5),
            ('b', 2, 5.1),
            ('c', 9, 4.3)]
    以上这种列表通过list.index无法查询，利用list.sort（或者sorted 函数）的 key 参数，
    通过提供一个函数来作为排序的依据来实现:
    temp.sort(key = lambda x:x[0]!='b') # temp[0] = ('b', 2, 5.1),
    findindex = lambda self,i,value:sorted(self,key=lambda x:x[i]!=value)[0]
    findindex(temp,0,'b')
    """
    lens = len(array)
    for i in range(lens-1):
        if num-array[i] in array:
            if array.count(num-array[i]) == 1 and num-array[i] == array[i]:
                continue
            else:
                j = array.index(num-array[i], i+1)
                break
    if j > 0:
        print([i, j])
    else:
        print([])

def two_sum_3(num, array):
    """
    同方法2，但是num-array[i]查找并非需要在array中全部遍历一遍，只需要在array[i]之前或者之后就可以。
    """
    lens = len(array)
    for i in range(1, lens):
        if num-array[i] in array[:i]:
            j = array[:i].index(num-array[i])
    print([j, i])

def two_sum_4(num,array):
    """
    通过哈希来求解，用字典来模拟哈希表，如果列表里的值有重复情况，
    转换成的key会有遗漏
    知识点：dict.get(key, default=None)
            key -- 字典中要查找的键。
            default -- 如果指定键的值不存在时，返回该默认值。
    """
    hashmap = {}
    for index, data in enumerate(array):
        hashmap[data] = index
    for i, data in enumerate(array):
        if num-data in hashmap:
            j = hashmap.get(num-data)
            if j and i < j:
                print([i, j])


def two_sum_5(num, array):
    """
    同方法4，但是不需要在整个字典内遍历，只需要在第二个数之前的dict内遍历一遍即可
    """
    hashmap = {}
    for i, data in enumerate(array):
        if num-data in hashmap:
            j = hashmap.get(num-data)
            print(j, i)  # j的顺序在i前面
        hashmap[data] = i

def main():
    num = 88
    array = [10, 60, 8, 18, 33, 48, 29, 99, 88, 28]
    # a = enumerate(array)
    # print(list(a))
    two_sum_5(num, array)


if __name__ == '__main__':
    main()
