#!/usr/bin/python3
# coding=utf-8

import os
import datetime
import platform
from collections import namedtuple
from jinja2 import Environment, FileSystemLoader

import global_config

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

        if (platform.system() != "Linux"):
            print("Host os is not supported.")
            self.disk_lst = [('253', '1', 'dm-1', '90', '0', '4920', '152', '0', '0', '0', '0', '0', '132','152'),
                             ('253', '0', 'dm-0', '8603', '0', '720365', '113780', '4409', '0', '84315', '47476', '0', '69038', '161258')]
            return

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

    def dump_logs(self, file_name=''):
        '''
        磁盘信息写文件
        :param file_name:
        :return:
        '''
        if file_name.strip() == '':
            file_name = datetime.datetime.now().strftime(
                './logs/%Y%m%d_%H%M%S_disk_info.csv')
        with open(file_name, "w", encoding='utf-8') as f:
            # title
            f.write(','.join(self.title.split()) + '\n')
            # content
            for i in self.disk_lst:
                f.write(','.join(i) + '\n')

    def dump_html(self):
        """
        Templates the given file with the keyword arguments.

        Args:
        in_file_path: The path to the template
        out_file_path: The path to output the templated file
        **kwargs: Variables to use in templating
        """
        in_file_path='./templates/tpl_disk_info.html'
        out_file_path='./reports/disk_info.html'
        kwargs={'title':'aa',
              'tb_title':self.title.split(),
              'tb_rows':self.disk_lst}
        env = Environment(loader=FileSystemLoader(os.path.dirname(in_file_path)),
                          keep_trailing_newline=True)
        template = env.get_template(os.path.basename(in_file_path))
        output = template.render(**kwargs)

        with open(out_file_path, mode="w", encoding='utf-8') as f:
            f.write(output) 



if __name__ == "__main__":
    cfg = global_config.qinju_config()
 
    disk_info = Disk_info()
    # disk_info.disp_all()
    # disk_info.disp('sda')
    disk_info.dump_logs()
    disk_info.dump_html()




    
