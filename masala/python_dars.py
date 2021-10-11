# -*- coding: utf-8 -*-
"""
Created on Sun Oct  10 00:25:54 2021

@author: DELL Erali Abdinazarov
"""

s = input("Satr kiriting: ")
unli_hariflar = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
undosh_hariflar = ['b', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'y', 'z', "g'", 'sh', 'ch', 'ng']
for x in s:
    if x == s[1]:
        break
    if x.lower() in undosh_hariflar:
        print(x, "undosh harifi bilan boshlangan")
    else:
        print(x, 'bunday undosh harifi yo\'q')
for y in s:
    if y == s[-1]:
        if y in unli_hariflar:
            print(y, "unli harifi bilan tugagan")
            break
        else:
            print(y, 'bunday unli harifi yo\'q')  