#!/usr/bin/env python

import psutil
import platform



class CPU_info:

    def __init__(self):
        # common properties
        self.cpu_times = psutil.cpu_times()
        self.cpu_logical_times = psutil.cpu_times(percpu=True)

        # verify...
        l = [x-x for x in self.cpu_logical_times[0]] # init zero
        for i in self.cpu_logical_times:
            m1 = map(lambda x,y: x+y, l , list(i))
            l = [x for x in m1]
        print(l)


        # python version
        major, minor, patchlevel = platform.python_version_tuple()


    def dump(self):
        print(self.cpu_times)
        print(self.cpu_logical_times)




def fun():
    cpuinfo = CPU_info()
    cpuinfo.dump()



if __name__ == "__main__":
    fun()


