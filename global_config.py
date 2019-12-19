#!/usr/bin/python3
# coding=utf-8

import os
import configparser

QINJU_CONFIG_FILE = r'./qinju.cfg'

class qinju_config:
    def __init__(self):
        if os.path.exists(QINJU_CONFIG_FILE):
            self.get_config(QINJU_CONFIG_FILE)
        else:
            print("读取配置文件[%s]失败。" % QINJU_CONFIG_FILE)

    def get_config(self, cfg_file):
        '''
        读取配置文件
        :param cfg_file: 配置文件名
        :return:
        '''
        config = configparser.ConfigParser()
        config.read(cfg_file)
        sections = config.sections()

        self.templates_path = config['PATH']['templates_path']
        self.reports_path = config['PATH']['reports_path']

        self.tpl_disk_info = config['TEMPLATE']['tpl_disk_info']
        self.rpt_disk_info = config['REPORT']['rpt_disk_info']


        
