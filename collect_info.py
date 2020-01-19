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
        '''
        >>> s = 'reg query "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings"  "abc bbc"  123 "cd aaa" 12s 23'
        >>> s1 = re.split(r'"([\w+|\\| ]+)+\"', s)
        >>> s1
['reg query ', 'HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\
\Internet Settings', '  ', 'abc bbc', '  123 ', 'cd aaa', ' 12s 23']

>>> s2 = re.sub(r'(\w+)', r'"\1"', s)
>>> s2
'"reg" "query" ""HKEY_CURRENT_USER"\\"Software"\\"Microsoft"\\"Windows"\\"Curren
tVersion"\\"Internet" "Settings""  ""abc" "bbc""  "123" ""cd" "aaa"" "12s" "23"'


        :param cmd_line:
        :return:
        '''
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
        查看用户列表，本地管理员，当前在线用户
        :return:
        '''
        self.exec_tpl("net user")
        self.exec_tpl("net localgroup administrators")
        self.exec_tpl("query user")

    def get_session(self):
        '''
        查看与本机连接客户端的会话
        todo: 需要管理员权限
        :return:
        '''
        pass
        # self.exec_tpl("net session")

    def get_netstat(self):
        '''
        查看本机的端口列表
        :return:
        '''
        self.exec_tpl("netstat -ano")

    def get_share(self):
        '''
        查看本机共享
        :return:
        '''
        self.exec_tpl("net share")
        self.exec_tpl("wmic share get name,path,status")

    def get_arp(self):
        '''
        查看ARP缓存表
        :return:
        '''
        self.exec_tpl("route print")
        self.exec_tpl("arp -a")

    def get_firewall(self):
        '''
        查看防火墙配置
        :return:
        '''
        self.exec_tpl("netsh firewall show config")

    def get_proxy(self):
        '''
        查看代理配置
        :return:
        '''
        self.exec_tpl('reg query "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings"')

    def execute_tqdm(self):
        '''
        tqdm执行进度
        :return:
        '''
        try:
            with tqdm.tqdm() as pbar:
                pbar.set_description("get_ipconfig()")
                pbar.update()
                self.get_ipconfig()  

                pbar.set_description("get_os()")
                pbar.update()
                self.get_os()  # 8s

                pbar.set_description("get_arch()")
                pbar.update()
                self.get_arch()  

                pbar.set_description("get_software()")
                pbar.update()
                self.get_software() # s

                pbar.set_description("get_local_service()")
                pbar.update()
                self.get_local_service()  

                pbar.set_description("get_task()")
                pbar.update()
                self.get_task()  

                pbar.set_description("get_startup()")
                pbar.update()
                self.get_startup()  

                pbar.set_description("get_schedual()")
                pbar.update()
                self.get_schedual()  

                pbar.set_description("get_statistics()")
                pbar.update()
                self.get_statistics()  

                pbar.set_description("get_user_list()")
                pbar.update()
                self.get_user_list()  

                pbar.set_description("get_session()")
                pbar.update()
                self.get_session()  

                pbar.set_description("get_netstat()")
                pbar.update()
                self.get_netstat()  

                pbar.set_description("get_share()")
                pbar.update()
                self.get_share()  

                pbar.set_description("get_firewall()")
                pbar.update()
                self.get_firewall()

                pbar.set_description("get_proxy()")
                pbar.update()
                self.get_proxy()



        except Exception as e:
            print("发生异常"+e)



if __name__ == "__main__":
    with open('./collect_info.txt', 'w',
              encoding="utf-8") as of:
        info = collect_info(of)
