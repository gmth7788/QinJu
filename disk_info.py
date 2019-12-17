#!/usr/bin/python3
# coding=utf-8

from collections import namedtuple


class Disk_info:
    '''
    获取磁盘信息
    self.disk_lst，磁盘信息列表，每条磁盘信息是一个元组。
    '''

    def __init__(self):
        self.title = '主设备号 次设备号 设备名称' \
                     ' 读次数 合并读次数 读扇区次数 读花费的毫秒数' \
                     ' 写次数 合并写次数 写扇区次数 写操作花费的毫秒数' \
                     ' 正在处理的输入输出请求数 输入输出操作花费的毫秒数' \
                     ' 输入输出操作花费的加权毫秒数'

        self.disk_lst = []
        with open('/proc/diskstats') as f:
            for line in f:
                self.disk_lst.append(tuple(line.split()))

    def disp_all(self):
        '''
        输出所有设备
        :return:
        '''
        disk = namedtuple('Disk', self.title)
        [print(disk(*i)) for i in self.disk_lst]

    def disp(self, device):
        '''
        按设备名输出
        :param device:
        :return:
        '''
        [print(i) for i in self.disk_lst if device in i]

    def dump(self, file_name=r'./disk_info.csv'):
        '''
        磁盘信息写文件
        :param file_name:
        :return:
        '''
        with open(file_name, "w") as f:
            # title
            f.write(','.join(self.title.split()) + '\n')
            # content
            for i in self.disk_lst:
                f.write(','.join(i) + '\n')


if __name__ == "__main__":
    disk_info = Disk_info()
    disk_info.disp_all()
    disk_info.disp('sda')
    disk_info.dump()
