import time
import os
import statistics as stat

class Runtime:
    def __init__(self):
        self.starttime = 0
        self.endtime = 0

        self.runtimes = []

    def runtime(self, starttime, endtime):
        runtime = endtime - starttime
        self.runtimes.append(runtime)
        return runtime

    def calc_avg(self, runtimes):
        return stat.mean(runtimes)

    def calc_med(selfself, runtimes):
        return stat.median(runtimes)

    def calc_hi(self, runtimes):
        return max(runtimes)

    def calc_lo(self, runtimes):
        return min(runtimes)