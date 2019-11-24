import time
import os
import analytics
import statistics as stat

class Runtime:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

        self.runtimes = []

    def runtime(self, starttime, endtime):
        runtime = endtime - starttime
        self.runtimes.append(runtime)
        return runtime

    def print_rt(self, runtimes):
        analytics.avg_rt = self.calc_avg(runtimes)

    def calc_avg(self, runtimes):
        return stat.mean(runtimes)

    def calc_med(selfself, runtimes):
        return stat.median(runtimes)

    def calc_hi(self, runtimes):
        return max(runtimes)

    def calc_lo(self, runtimes):
        return min(runtimes)