#!/usr/bin/python3
# coding=utf-8

'''
https://www.qqxiuzi.cn/bianma/kaisamima.php
凯撒密码加密解密
'''


def caesar_cipher(info):
    info = str.upper(info)
    t1 = [chr(x+ord('A')) for x in range(26)]
    for i in range(26):
        t2 = [chr((x % 26)+ord('A')) for x in range(i, i+26)]
        d = dict(zip(t1, t2))

        s = ""
        for j in info:
            if str.isalpha(j):
                s += d[j]
            elif str.isspace(j):
                s += ' '
        print("{0}:{1}".format(i, s))
        print("\n\n\n")



if __name__ == "__main__":
    # caesar_cipher("FTQ CGUOW NDAIZ RAJ VGYBE AHQD FTQ XMLK PAS AR OMQEMD MZP KAGD GZUCGQ EAXGFUAZ UE ZOZYOPTMBXOA")

    caesar_cipher("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG OF CAESAR AND YOUR UNIQUE SOLUTION IS NCNMCDHAPLCO")
