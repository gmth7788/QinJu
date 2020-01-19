#!/usr/bin/python3
# coding=utf-8


import subprocess
import os
from random import random, randint

# pip install tqdm
import tqdm


class collect_info:
    def __init__(self, of):
        self.of = of
        self.execute_tqdm()

    def exec_tpl(self, cmd_line):
        cmd_lst = cmd_line.split(' ')
        self.of.write("\n" * 3 + "*" * 40 + "\n")
        self.of.write("> {0} \n".format(cmd_line))
        self.of.flush()
        ret = subprocess.call(cmd_lst,
                              stdin=None,
                              stdout=self.of,
                              stderr=None,
                              shell=False)

    def get_ipconfig(self):
        '''
        查询网络配置信息
        :return:
        '''
        self.exec_tpl("ipconfig /all")

    def get_os(self):
        '''
        查询操作系统及安装软件的版本信息
        :return:
        '''
        self.exec_tpl("systeminfo")

    def get_arch(self):
        '''
        查看系统体系结构（获取环境变量）
        :return:
        '''
        self.of.write("\n" * 3 + "*" * 40 + "\n")
        self.of.write('> echo %PROCESSOR_ARCHITECTURE% \n')
        self.of.flush()
        self.of.write(os.environ["PROCESSOR_ARCHITECTURE"])

    def get_software(self):
        '''
        查看安装的软件版本和路径
        :return:
        '''
        # self.exec_tpl('powershell "Get-WmiObject -class Win32_product | Select-Object -Property name, version"')
        self.exec_tpl("wmic product get name,version")

    def get_local_service(self):
        '''
        查询本机服务
        :return:
        '''
        self.exec_tpl("wmic service list brief")

    def get_task(self):
        '''
        查询进程列表
        :return:
        '''
        self.exec_tpl("tasklist /v")
        self.exec_tpl("wmic process list brief")

    def get_startup(self):
        '''
        查看启动程序信息
        :return:
        '''
        self.exec_tpl("wmic startup get command,caption")

    def get_schedual(self):
        '''
        查看计划任务
        :return:
        '''
        os.system("chcp 437")
        self.exec_tpl("schtasks /query /fo LIST /v")
        os.system("chcp 936")

    def get_statistics(self):
        '''
        查看主机开机时间
        :return:
        '''
        self.exec_tpl("net statistics workstation")

    def get_user_list(self):
        '''
        查看用户列表
        :return:
        '''
        self.exec_tpl("net user")

    def execute_tqdm(self):
        '''
        tqdm执行进度
        :return:
        '''
        with tqdm.tqdm() as pbar:
            pbar.set_description("get_ipconfig()")
            pbar.update()
            self.get_ipconfig()  # 1s

            pbar.set_description("get_os()")
            pbar.update()
            self.get_os()  # 8s

            pbar.set_description("get_arch()")
            pbar.update()
            self.get_arch()  # 1s

            pbar.set_description("get_software()")
            pbar.update()
            self.get_software() # s

            pbar.set_description("get_local_service()")
            pbar.update()
            self.get_local_service()  # 1s

            pbar.set_description("get_task()")
            pbar.update()
            self.get_task()  # 1s

            pbar.set_description("get_startup()")
            pbar.update()
            self.get_startup()  # 1s

            pbar.set_description("get_schedual()")
            pbar.update()
            self.get_schedual()  # 1s

            pbar.set_description("get_statistics()")
            pbar.update()
            self.get_statistics()  # 1s

            pbar.set_description("get_user_list()")
            pbar.update()
            self.get_user_list()  # 1s


if __name__ == "__main__":
    with open('./collect_info.txt', 'w',
              encoding="utf-8") as of:
        info = collect_info(of)
