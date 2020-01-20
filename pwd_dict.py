#!/usr/bin/python3
# coding=utf-8

import itertools as its


def gen_pwd_dict(file_name=r'./pwd.txt'):

    words="abcdefghijklmnopqrstuvwxyz"
    dic=open(file_name, 'w')
    for num in range(6,10):
        keys=its.product(words,repeat=num)
        for key in keys:
            dic.write("".join(key)+"\n")
    dic.close()


if __name__ == "__main__":
    cfg = gen_pwd_dict(r"./pwd.txt")
