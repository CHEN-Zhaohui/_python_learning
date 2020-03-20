# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 22:00:37 2020

@author: Chen Zhaohui
"""

mm = [
    ['6','8','2'],
    ['6','1','4'],
    ['2','0','6'],
    ['7','3','8'],
    ['8','7','0']
]

def check1(i,j,z):
    if i==mm[0][0] and (mm[0][1] not in Str) and (mm[0][2] not in Str):
        return True
    if j == mm[0][1] and (mm[0][0] not in Str) and (mm[0][2] not in Str):
        return True
    if z == mm[0][2] and (mm[0][0] not in Str) and (mm[0][1] not in Str):
        return True
    return False

def check2(i,j,z):
    if (mm[1][0] in Str) and (i!=mm[1][0]):
        return True
    if (mm[1][1] in Str) and (j!=mm[1][1]):
        return True
    if (mm[1][2] in Str) and (z!=mm[1][2]):
        return True
    return False

def check3(i ,j ,z):
    if (mm[2][0] in Str) and (mm[2][1] in Str) and i!=mm[2][0] and j!=mm[2][1]:
        return True
    if (mm[2][0] in Str) and (mm[2][2] in Str) and i!=mm[2][0] and z!=mm[2][2]:
        return True
    if (mm[2][2] in Str) and (mm[2][1] in Str) and j!=mm[2][1] and z!=mm[2][2]:
        return True
    return False

def check4(i, j ,z):
    if (mm[3][0] not in Str) and (mm[3][1] not in Str) and (mm[3][2] not in Str):
        return True
    return False
def check5(i ,j ,z):
    if (mm[4][0] in Str) and (i!=mm[4][0]):
        return True
    if (mm[4][1] in Str) and (j!=mm[4][1]):
        return True
    if (mm[4][2] in Str) and (z!=mm[4][2]):
        return True
    return False

if __name__ == '__main__':
    for i in range(10):
        i = str(i)
        for j in range(10):
            j = str(j)
            for z in range(10):
                z = str(z)
                Str = i + j + z
                if check1(i, j, z):
                    if check2(i,j,z):
                        if check3(i, j, z):
                            if check4(i, j, z):
                                if check5(i, j, z):
                                    print(Str)
                                    